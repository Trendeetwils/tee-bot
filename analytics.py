"""
analytics.py — Supabase analytics for both Faith and Matrix modes
"""
import os, requests
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

def _h():
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

def ok():
    return bool(SUPABASE_URL and SUPABASE_KEY)

def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")

def track_user(user_id: int, username: str, first_name: str) -> bool:
    if not ok(): return False
    try:
        r = requests.get(
            f"{SUPABASE_URL}/rest/v1/users?user_id=eq.{user_id}&select=user_id",
            headers=_h(), timeout=5)
        if len(r.json()) == 0:
            requests.post(f"{SUPABASE_URL}/rest/v1/users", headers=_h(),
                json={"user_id": user_id, "username": username or "",
                      "first_name": first_name or "", "joined": today()}, timeout=5)
            _event(user_id, "new_user", first_name or str(user_id))
            return True
        return False
    except Exception as e:
        print(f"[Analytics] track_user: {e}")
        return False

def track_message(user_id: int):
    if not ok(): return
    try:
        requests.post(f"{SUPABASE_URL}/rest/v1/rpc/increment_messages",
            headers=_h(), json={"uid": user_id}, timeout=5)
    except Exception as e:
        print(f"[Analytics] track_message: {e}")

def track_faith_test(user_id: int, label: str, pct: int, religion: str, tone: str):
    if not ok(): return
    try:
        r = requests.get(f"{SUPABASE_URL}/rest/v1/users?user_id=eq.{user_id}&select=faith_tests",
            headers=_h(), timeout=5)
        d = r.json()
        current = d[0].get("faith_tests", 0) if d else 0
        requests.patch(f"{SUPABASE_URL}/rest/v1/users?user_id=eq.{user_id}",
            headers=_h(),
            json={"faith_tests": current+1, "faith_last_score": pct,
                  "faith_last_result": label, "faith_religion": religion,
                  "faith_tone": tone, "active_mode": "faith",
                  "updated_at": datetime.now(timezone.utc).isoformat()}, timeout=5)
        _event(user_id, "faith_test", f"{label} — {pct}% — {religion}")
    except Exception as e:
        print(f"[Analytics] track_faith_test: {e}")

def track_matrix_test(user_id: int, label: str, pct: int, tone: str):
    if not ok(): return
    try:
        r = requests.get(f"{SUPABASE_URL}/rest/v1/users?user_id=eq.{user_id}&select=matrix_tests",
            headers=_h(), timeout=5)
        d = r.json()
        current = d[0].get("matrix_tests", 0) if d else 0
        requests.patch(f"{SUPABASE_URL}/rest/v1/users?user_id=eq.{user_id}",
            headers=_h(),
            json={"matrix_tests": current+1, "matrix_last_score": pct,
                  "matrix_last_result": label, "matrix_tone": tone,
                  "active_mode": "matrix",
                  "updated_at": datetime.now(timezone.utc).isoformat()}, timeout=5)
        _event(user_id, "matrix_test", f"{label} — {pct}%")
    except Exception as e:
        print(f"[Analytics] track_matrix_test: {e}")

def _event(user_id: int, etype: str, detail: str):
    if not ok(): return
    try:
        requests.post(f"{SUPABASE_URL}/rest/v1/events", headers=_h(),
            json={"user_id": user_id, "event_type": etype, "detail": detail}, timeout=5)
    except: pass

def get_stats() -> dict:
    if not ok(): return {"error": "Supabase not configured"}
    try:
        r = requests.get(f"{SUPABASE_URL}/rest/v1/users?select=*",
            headers=_h(), timeout=8)
        users = r.json()
        total = len(users)
        new_today = sum(1 for u in users if u.get("joined") == today())
        week_ago = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
        active_7d = sum(1 for u in users if u.get("updated_at","") > week_ago)
        total_msg = sum(u.get("messages",0) for u in users)
        total_faith = sum(u.get("faith_tests",0) for u in users)
        total_matrix = sum(u.get("matrix_tests",0) for u in users)

        # Result breakdowns
        faith_results = {}
        matrix_results = {}
        religion_picks = {}
        for u in users:
            fr = u.get("faith_last_result")
            mr = u.get("matrix_last_result")
            rel = u.get("faith_religion")
            if fr: faith_results[fr] = faith_results.get(fr,0)+1
            if mr: matrix_results[mr] = matrix_results.get(mr,0)+1
            if rel: religion_picks[rel] = religion_picks.get(rel,0)+1

        return {
            "total_users": total,
            "new_today": new_today,
            "active_7d": active_7d,
            "total_messages": total_msg,
            "total_faith_tests": total_faith,
            "total_matrix_tests": total_matrix,
            "top_faith_result": max(faith_results, key=faith_results.get) if faith_results else "N/A",
            "top_matrix_result": max(matrix_results, key=matrix_results.get) if matrix_results else "N/A",
            "top_religion": max(religion_picks, key=religion_picks.get) if religion_picks else "N/A",
            "faith_breakdown": faith_results,
            "matrix_breakdown": matrix_results,
            "religion_breakdown": religion_picks,
        }
    except Exception as e:
        return {"error": str(e)}

def track_deep_dive_unlock(user_id: int):
    if not ok(): return
    try:
        requests.patch(
            f"{SUPABASE_URL}/rest/v1/users?user_id=eq.{user_id}",
            headers=_h(),
            json={"deep_dive_unlocked": True,
                  "updated_at": datetime.now(timezone.utc).isoformat()},
            timeout=5
        )
        _event(user_id, "deep_dive_unlock", "Unlocked deep dive mode")
    except Exception as e:
        print(f"[Analytics] deep_dive: {e}")

def get_recent_users(limit=10) -> list:
    if not ok(): return []
    try:
        r = requests.get(
            f"{SUPABASE_URL}/rest/v1/users?select=*&order=joined.desc&limit={limit}",
            headers=_h(), timeout=5)
        return r.json()
    except: return []