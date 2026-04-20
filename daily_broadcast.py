"""
daily_broadcast.py
==================
Sends a daily provocative question to @teetheredpill channel.

TO ACTIVATE:
1. Add the bot as ADMIN in @teetheredpill channel
   - Open the channel → Admins → Add Admin → search @honestteebot
   - Give it permission to "Post Messages"
2. Set BROADCAST_CHANNEL=@teetheredpill in Render environment variables
"""

import os, random
from dotenv import load_dotenv

load_dotenv()
BROADCAST_CHANNEL = os.getenv("BROADCAST_CHANNEL", "")

DAILY_DROPS = [
    # Faith
    ("🛐", "If God is all-powerful and all-loving — why do innocent children get cancer?", "faith"),
    ("📖", "The Bible has been rewritten over 450 times. Which version is the real word of God?", "faith"),
    ("🛐", "Muhammad married a 9-year-old. Does that disqualify him as a moral guide?", "faith"),
    ("📖", "Christmas trees, Easter eggs — both come from pagan traditions. Does your faith know?", "faith"),
    ("🛐", "If God knows everything you'll do before you're born — is punishing you even fair?", "faith"),
    ("📖", "The Council of Nicaea in 325 AD — humans voted on what goes in the Bible. Comfortable with that?", "faith"),
    ("🛐", "Islam spread across Africa largely by conquest. Does a religion of peace do that?", "faith"),
    ("📖", "Hell — eternal torture for a short life. Is that justice or a control mechanism?", "faith"),
    ("🛐", "Both Islam and Christianity say only their followers go to heaven. Both can't be right. So?", "faith"),
    ("📖", "Teaching children they are born sinful — is that faith or psychological damage?", "faith"),
    # Matrix
    ("🔴", "Most people are living a life someone else designed for them. Are you one of them?", "matrix"),
    ("🧠", "Hard work alone leads to success. True — or the biggest lie you were sold?", "matrix"),
    ("🔴", "If you died tomorrow — would you say you actually lived?", "matrix"),
    ("🧠", "The version of you on social media vs who you are at 2am. How different are they?", "matrix"),
    ("🔴", "Most people know exactly what they need to do to improve their life. They just don't do it. Why?", "matrix"),
    ("🧠", "Your 5 closest friends — do you like who their average makes you?", "matrix"),
    ("🔴", "Africa is the most religious continent and one of the poorest. Coincidence?", "matrix"),
    ("🧠", "Comfort is the enemy of growth. Do you live by that — or just agree with it?", "matrix"),
    ("🔴", "What is the one thing you know you should do but keep finding reasons not to?", "matrix"),
    ("🧠", "How much of your personality is authentically yours — vs shaped by where you grew up?", "matrix"),
]

def get_daily_drop():
    return random.choice(DAILY_DROPS)

async def broadcast(bot):
    if not BROADCAST_CHANNEL:
        print("[Broadcast] No channel set — skipping")
        return

    emoji, question, qtype = get_daily_drop()
    mode_label = "KNOW YOUR FAITH" if qtype == "faith" else "KNOW THE MATRIX"
    cta = "Take the full test 👇" if qtype == "faith" else "How aware are you really? 👇"

    text = (
        f"{emoji} *{mode_label}*\n\n"
        f"*{question}*\n\n"
        f"_{cta}_\n"
        f"👉 t.me/honestteebot\n\n"
        f"📢 @teetheredpill"
    )

    try:
        await bot.send_message(
            chat_id=BROADCAST_CHANNEL,
            text=text,
            parse_mode="Markdown"
        )
        print(f"[Broadcast] Sent to {BROADCAST_CHANNEL}")
    except Exception as e:
        print(f"[Broadcast] Failed: {e}")
        # Common fix hint
        if "chat not found" in str(e).lower() or "forbidden" in str(e).lower():
            print("[Broadcast] Make sure the bot is an ADMIN in the channel with post permission")
