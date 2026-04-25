"""
reengagement.py
================
Pings inactive users after 2-5 days of no activity.
Runs as a daily job — checks who hasn't chatted and sends them a nudge.

IMPORTANT — Telegram rules:
- Users must have messaged the bot first (they have)
- Cannot send bulk spam — messages must feel personal
- One message per inactive period — never back to back
- Users can /stop at any time to opt out
"""

import os, random
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

load_dotenv()

# ── Message templates — feel personal, not automated ─────────────────────────

FAITH_NUDGES = [
    "👀 Hey — you left mid-thought last time.\n\nI've got a question that's been sitting here:\n\n*If God knew you'd doubt him before you were born — is punishing you for it still fair?*\n\nThink about it. Reply when you're ready.",
    "🔥 Quick one.\n\n*The Bible has been rewritten 450+ times.*\n\nWhich version is the actual word of God?\n\nSeriously — nobody ever answers this properly.",
    "📖 Something I've been thinking about.\n\nBoth Islam and Christianity promise heaven.\nBoth threaten hell.\nBoth claim to be the only true path.\n\n*They can't both be right. So what does that mean?*\n\nCome argue with me.",
    "💀 Real question:\n\n*If prayer worked — hospitals would be empty.*\n\nWhy doesn't it work that way?\n\nI'm ready when you are.",
    "👁️ Here's something nobody talks about.\n\nThe same God who watched slavery, genocide, and child abuse for thousands of years — *did nothing.*\n\nHow do you make peace with that?\n\nSeriously asking.",
]

MATRIX_NUDGES = [
    "🔴 Something to think about.\n\n*Most people are living a life someone else designed for them.*\n\nAre you one of them?\n\nCome back and let's talk about it.",
    "🧠 Quick question.\n\n*If you died tomorrow — would you say you actually lived?*\n\nNot trying to be dark. Just think it's worth answering honestly.",
    "⚡ Still thinking about your Matrix score.\n\n*The biggest gap isn't between knowing and not knowing.*\n*It's between knowing and actually doing.*\n\nWhat's yours right now?",
    "🔴 One thing.\n\n*Hard work alone doesn't lead to success.*\n*Timing, positioning, and who you know matter more than anyone admits.*\n\nAsk me about the real formula.",
    "💡 Real talk.\n\n*Your 5 closest friends shape who you are more than any book or course.*\n\nDo you like who that average makes you?\n\nCome back — let's get into it.",
]

GENERAL_NUDGES = [
    "Hey 👋\n\nIt's been a few days.\n\nAnything on your mind — faith, life, or just something you've been questioning?\n\nI'm here.",
    "🔴 Quick check in.\n\nYou haven't finished the other test yet.\n\nType /test — takes 2 minutes. Might surprise you.",
    "👀 Still thinking about your result?\n\nMost people are.\n\nAsk me anything — I don't bite. I just don't sugarcoat either.",
]

def get_nudge_message(user_data: dict) -> str:
    """Pick the right nudge based on what the user has done"""
    faith_score  = user_data.get("faith_last_score")
    matrix_score = user_data.get("matrix_last_score")

    if faith_score and not matrix_score:
        # Has Faith score but not Matrix — nudge toward Matrix
        msg = random.choice(FAITH_NUDGES)
        msg += "\n\n_Also — have you tried the Matrix test yet? Type /test_"
        return msg
    elif matrix_score and not faith_score:
        # Has Matrix score but not Faith — nudge toward Faith
        msg = random.choice(MATRIX_NUDGES)
        msg += "\n\n_Also — try the Faith test if you haven't. Type /test_"
        return msg
    elif faith_score:
        return random.choice(FAITH_NUDGES)
    elif matrix_score:
        return random.choice(MATRIX_NUDGES)
    else:
        return random.choice(GENERAL_NUDGES)

async def send_reengagement_messages(bot, supabase_url: str, supabase_key: str):
    """Find inactive users and send them a nudge"""
    import requests

    if not supabase_url or not supabase_key:
        print("[Reengagement] Supabase not configured — skipping")
        return

    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
    }

    # Find users inactive for 2-5 days who haven't been nudged recently
    now = datetime.now(timezone.utc)
    cutoff_recent = (now - timedelta(days=2)).isoformat()   # inactive at least 2 days
    cutoff_old    = (now - timedelta(days=5)).isoformat()   # not more than 5 days

    try:
        # Get users updated between 2 and 5 days ago
        r = requests.get(
            f"{supabase_url}/rest/v1/users"
            f"?updated_at=lte.{cutoff_recent}"
            f"&updated_at=gte.{cutoff_old}"
            f"&select=user_id,first_name,faith_last_score,matrix_last_score,last_nudged",
            headers=headers,
            timeout=10
        )
        users = r.json()
        if not isinstance(users, list):
            print(f"[Reengagement] Unexpected response: {users}")
            return

        print(f"[Reengagement] Found {len(users)} inactive users to nudge")

        sent = 0
        for user in users:
            user_id = user.get("user_id")
            if not user_id:
                continue

            # Don't nudge if already nudged in the last 5 days
            last_nudged = user.get("last_nudged")
            if last_nudged:
                last_nudged_dt = datetime.fromisoformat(last_nudged.replace("Z", "+00:00"))
                if (now - last_nudged_dt).days < 5:
                    continue

            # Send the nudge
            try:
                msg = get_nudge_message(user)
                await bot.send_message(
                    chat_id=user_id,
                    text=msg,
                    parse_mode="Markdown"
                )

                # Record that we nudged this user
                requests.patch(
                    f"{supabase_url}/rest/v1/users?user_id=eq.{user_id}",
                    headers={**headers, "Prefer": "return=minimal"},
                    json={"last_nudged": now.isoformat()},
                    timeout=5
                )
                sent += 1
                print(f"[Reengagement] Nudged user {user_id} ({user.get('first_name','')})")

                # Small delay between messages to avoid rate limiting
                import asyncio
                await asyncio.sleep(0.5)

            except Exception as e:
                err = str(e)
                if "blocked" in err.lower() or "forbidden" in err.lower() or "deactivated" in err.lower():
                    print(f"[Reengagement] User {user_id} blocked bot or deactivated")
                else:
                    print(f"[Reengagement] Failed to nudge {user_id}: {e}")

        print(f"[Reengagement] Done — sent {sent} nudges")

    except Exception as e:
        print(f"[Reengagement] Error: {e}")
