"""
reengagement.py — Pings inactive users after 2-5 days
First message is always general. Follow-ups are religion/mode specific.
"""

import os, random, asyncio, requests
from datetime import datetime, timezone, timedelta

# ── FIRST MESSAGE — always general, warm, curiosity-driven ───────────────────

FIRST_NUDGES = [
    "Hey 👋\n\nIt's been a few days.\n\nAnything you've been thinking about — faith, life, something someone said that stuck with you?\n\nI'm here. No pressure.",
    "🔴 Quick check in.\n\nYou took the test a few days ago.\n\nHave you thought about your result since then?\n\nMost people do — and have questions after. What's yours?",
    "Hey 👋 Been a while.\n\nYou haven't tried the other test yet.\n\nType /test — takes 2 minutes. People say it hits different the second time.",
    "👁️ Something worth asking yourself today:\n\n*What's one thing you believe strongly — that you've never actually questioned?*\n\nJust sit with it. No wrong answer.",
    "🔴 One question.\n\n*Is the life you're living the one you chose — or the one that happened to you?*\n\nNo rush. Just think about it.",
]

# ── FAITH FOLLOW-UP — by religion ────────────────────────────────────────────

CHRISTIANITY_NUDGES = [
    "📖 Something that doesn't get discussed enough.\n\nThe Bible has been rewritten *450+ times* by human hands.\n\nWhich version is the actual word of God?\n\nSeriously — nobody ever answers this properly.",
    "✝️ Real question.\n\n*If God knew before you were born that you'd sin and end up in hell — why create you?*\n\nIs that love — or a setup?",
    "💀 The Trinity.\n\nFather, Son, and Holy Spirit — *one* God.\n\nIf Jesus prayed to God — was he praying to himself?\n\nThis one bothers more Christians than they admit.",
    "📖 Hebrews 9:22 — *without the shedding of blood there is no forgiveness.*\n\nWhy would an all-powerful God need blood to forgive?\n\nThat sounds more like a pagan ritual than a loving father.",
    "✝️ Christmas trees. Easter eggs. The name Easter itself.\n\nAll from pagan traditions — rebranded.\n\n*How much of Christianity is original?*",
]

ISLAM_NUDGES = [
    "☪️ Quran 4:34 allows men to beat their wives.\n\nScholars say it means a *light tap*.\n\n*But why would a loving God include that instruction at all?*\n\nSeriously.",
    "📖 The Quran says the sun sets in a muddy spring (18:86).\n\nThe creator of the universe — got where the sun goes wrong?\n\nHow do you explain that?",
    "☪️ Islam spread across Arabia, Africa, and Persia *largely through military conquest*.\n\n*Does a religion of peace spread by the sword?*\n\nCome argue with me.",
    "💀 Leaving Islam can carry the death penalty in many Islamic teachings.\n\n*A religion you cannot leave without dying is not a religion. It's a prison.*\n\nWhat do you think?",
    "📖 Muhammad received all his revelations *alone* — no witnesses.\n\nEvery religion started with one person's unverifiable private claim.\n\nWhat makes this one different?",
]

HINDUISM_NUDGES = [
    "🕉️ The caste system — dividing humans by birth into a hierarchy of worth.\n\n*Divinely ordained suffering for sins in a past life you can't remember.*\n\nIs that justice — or the most effective poverty trap ever invented?",
    "🕉️ Karma teaches that suffering in this life comes from a past life.\n\n*Does that mean victims of abuse or poverty deserve it?*\n\nThink about what that framework actually does to real people.",
    "📖 Reincarnation — cycling through millions of births.\n\n*Has anyone come back to confirm it?*\n\nWhat evidence beyond ancient texts do we have?",
]

# ── MATRIX FOLLOW-UP ──────────────────────────────────────────────────────────

MATRIX_NUDGES = [
    "🔴 Still thinking about your Matrix score.\n\n*The biggest gap isn't between knowing and not knowing.*\n*It's between knowing — and actually doing something about it.*\n\nWhat's yours right now?",
    "🧠 One thing.\n\n*Your 5 closest friends shape who you become more than any book or mentor.*\n\nDo you like who that average makes you?\n\nCome back — let's get into it.",
    "⚡ Real question.\n\n*Hard work alone doesn't lead to success.*\n\nTiming, positioning, and access matter more than most people admit.\n\nAsk me about the real formula.",
    "🔴 Quick one.\n\n*If you died tomorrow — would you say you actually lived?*\n\nNot trying to be dark. Just think it's worth answering honestly.",
    "💡 Something to consider.\n\n*Most people are living a life someone else designed for them.*\n\nSchool told you what to learn.\nSociety told you what success looks like.\nReligion told you what to fear.\n\n*What did YOU actually decide?*",
]

def get_nudge(user: dict, is_first: bool) -> str:
    if is_first:
        return random.choice(FIRST_NUDGES)

    religion = user.get("faith_religion", "")
    faith_score = user.get("faith_last_score")
    matrix_score = user.get("matrix_last_score")
    active_mode = user.get("active_mode", "faith")

    if active_mode == "matrix" or (matrix_score and not faith_score):
        return random.choice(MATRIX_NUDGES)

    if religion == "islam":
        return random.choice(ISLAM_NUDGES)
    elif religion == "hinduism":
        return random.choice(HINDUISM_NUDGES)
    else:
        # Default to Christianity nudges for all faith users
        return random.choice(CHRISTIANITY_NUDGES)

async def send_reengagement_messages(bot, supabase_url: str, supabase_key: str):
    if not supabase_url or not supabase_key: 
        print("[Reengagement] Supabase not configured — skipping")
        return

    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
    }
 
    now = datetime.now(timezone.utc)
    cutoff_recent = (now - timedelta(days=2)).isoformat()
    cutoff_old    = (now - timedelta(days=5)).isoformat()

    try: 
        r = requests.get(
            f"{supabase_url}/rest/v1/users"
            f"?updated_at=lte.{cutoff_recent}"
            f"&updated_at=gte.{cutoff_old}"
            f"&select=user_id,first_name,faith_last_score,matrix_last_score,"
            f"faith_religion,active_mode,last_nudged",
            headers=headers, timeout=10
        )
        users = r.json()
        if not isinstance(users, list):
            print(f"[Reengagement] Bad response: {users}")
            return

        print(f"[Reengagement] {len(users)} inactive users found")
        sent = 0

        for user in users:
            user_id = user.get("user_id")
            if not user_id:
                continue
 
            last_nudged = user.get("last_nudged")
            is_first = not bool(last_nudged)

            if last_nudged:
                try:
                    last_dt = datetime.fromisoformat(last_nudged.replace("Z", "+00:00"))
                    if (now - last_dt).days < 5:
                        continue
                except Exception:
                    pass

            try: 
                msg = get_nudge(user, is_first)
                await bot.send_message(
                    chat_id=user_id,
                    text=msg,
                    parse_mode="Markdown"
                ) 
                requests.patch(
                    f"{supabase_url}/rest/v1/users?user_id=eq.{user_id}",
                    headers={**headers, "Prefer": "return=minimal"},
                    json={"last_nudged": now.isoformat()},
                    timeout=5
                )
                sent += 1
                print(f"[Reengagement] Nudged {user.get('first_name',user_id)}")
                await asyncio.sleep(0.5)

            except Exception as e:
                err = str(e).lower()
                if any(x in err for x in ["blocked","forbidden","deactivated","not found"]):
                    print(f"[Reengagement] User {user_id} unreachable")
                else:
                    print(f"[Reengagement] Error for {user_id}: {e}")

        print(f"[Reengagement] Done — {sent} nudges sent")

    except Exception as e:
        print(f"[Reengagement] Fatal error: {e}")