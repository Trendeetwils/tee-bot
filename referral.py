"""
referral.py — Tracks referrals per user in a simple JSON file
             + streak system for daily retention
"""

import json
import os
from datetime import date, timedelta

REFERRAL_FILE = "referrals.json"
STREAK_FILE   = "streaks.json"
UNLOCK_THRESHOLD = 3  # friends needed to unlock deep dive


# ── Referral helpers ───────────────────────────────────────────────────────────

def _load():
    if not os.path.exists(REFERRAL_FILE):
        return {}
    with open(REFERRAL_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(REFERRAL_FILE, "w") as f:
        json.dump(data, f)

def get_referral_link(bot_username: str, user_id: int) -> str:
    return f"https://t.me/{bot_username}?start=ref_{user_id}"

def record_referral(referred_by: int):
    data = _load()
    key = str(referred_by)
    data[key] = data.get(key, 0) + 1
    _save(data)

def get_referral_count(user_id: int) -> int:
    data = _load()
    return data.get(str(user_id), 0)

def is_unlocked(user_id: int) -> bool:
    return get_referral_count(user_id) >= UNLOCK_THRESHOLD


# ── Streak helpers ─────────────────────────────────────────────────────────────

def _load_streaks():
    if not os.path.exists(STREAK_FILE):
        return {}
    with open(STREAK_FILE, "r") as f:
        return json.load(f)

def _save_streaks(data):
    with open(STREAK_FILE, "w") as f:
        json.dump(data, f)

def check_and_update_streak(user_id: int):
    """
    Call once per incoming message/start.
    Returns (streak_count: int, is_new_day: bool).
    - is_new_day=True  → first interaction today; show the streak message.
    - is_new_day=False → already counted today; stay silent.
    """
    data      = _load_streaks()
    key       = str(user_id)
    today     = str(date.today())
    yesterday = str(date.today() - timedelta(days=1))

    entry     = data.get(key, {"streak": 0, "last_date": ""})
    last_date = entry.get("last_date", "")
    streak    = entry.get("streak", 0)

    if last_date == today:
        # Already logged today — don't double-count or re-show banner
        return streak, False

    if last_date == yesterday:
        streak += 1          # kept the chain alive
    else:
        streak = 1           # gap detected — reset

    data[key] = {"streak": streak, "last_date": today}
    _save_streaks(data)
    return streak, True


def streak_message(streak: int) -> str:
    """Return the streak banner text, or '' if streak < 2."""
    if streak < 2:
        return ""
    fire = "🔥" * min(streak, 5)          # cap fire emojis at 5
    if streak == 2:
        flavour = "Two days in. You might be serious about this."
    elif streak == 3:
        flavour = "Three days straight. You're hooked. 😏"
    elif streak == 7:
        flavour = "A full week. Most people quit by day two."
    elif streak == 30:
        flavour = "30 days. You've fully swallowed the red pill. 🔴"
    else:
        flavour = "Keep going."
    return f"Day {streak} {fire} — you're on a streak.\n_{flavour}_\n\n"