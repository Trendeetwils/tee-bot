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
    ("📖", "The flood story in the Bible?\n\nIt appears in the Babylonian *Epic of Gilgamesh* — written 1000 years earlier.\n\n*Did God recycle the script?*", "faith"),
    ("📖", "The Bible has been rewritten over 450 times. Which version is the real word of God?", "faith"),
    ("😔", "Some of the most religious people on earth are also the poorest.\n\n*Is God testing them — or has religion taught them to accept what they should be fighting?*", "faith"),
    ("💸", "Prosperity gospel pastors preach that *faith brings wealth.*\n\nTheir congregations are poor. The pastor drives a Rolls Royce.\n\n*Whose faith is actually working here?*", "faith"),
    ("😔", "If God sees every sparrow that falls — does he also see every child that starves?\n\nAnd if he sees it — *why doesn't he stop it?*\n\nThe free will argument doesn't cover hunger.", "faith"),
    ("🛐", "Muhammad married a 9-year-old. Does that disqualify him as a moral guide?", "faith"),
    ("📖", "The Bible says God is unchanging (Malachi 3:6).\nThe Bible says God regretted creating humans (Genesis 6:6).\n\n*An unchanging God who has regrets is a contradiction.*\n\nWhich verse do you follow?", "faith"),
    ("📖", "Christmas trees, Easter eggs — both come from pagan traditions. Does your faith know?", "faith"),
     ("🚗", "You survived a car crash that killed the other driver.\n\nWas God protecting you?\n\n*If yes — what did the other driver do wrong?*", "faith"),
    ("✈️", "A plane crashes. 200 people die. 3 survive.\n\nThe 3 survivors say *God saved me.*\n\n*What did God say to the other 200?*", "faith"),
    ("🚗", "You survived something that should have killed you.\n\nMost people call that a miracle.\n\n*But if God chooses who survives — he also chooses who doesn't.*\n\nIs that the God you believe in?", "faith"),
    ("🛐", "If God knows everything you'll do before you're born — is punishing you even fair?", "faith"),
     ("🏥", "You got sick. The doctor treated you. You recovered.\n\nWho do you thank first — *God or the doctor?*\n\nAnd if God gets the credit — what does the doctor get?", "faith"),
    ("💊", "Doctors spend 10+ years training to save lives.\n\nYou're on the operating table.\n\nIs the scalpel guided by God — or by a human who studied anatomy for a decade?", "faith"),
    ("🏥", "Every time medicine saves someone — believers say *God healed them.*\n\nWhen it doesn't work — they say *God called them home.*\n\n*God wins either way. The doctor gets nothing.*\n\nDoes that seem fair?", "faith"),
    ("📖", "The Council of Nicaea in 325 AD — humans voted on what goes in the Bible. Comfortable with that?", "faith"),
    ("🛐", "Islam spread across Africa largely by conquest. Does a religion of peace do that?", "faith"),
    ("💀", "When a child dies from cancer — people say *it was God's will.*\n\nWhen a doctor saves a child — people say *God is good.*\n\n*Which one is actually God's will?*", "faith"),
    ("💀", "If God controls when you die — why do people go to hospital?\n\nIf it's your time — the hospital won't help.\n\nIf it's not — you don't need it.\n\n*So what exactly is medicine for?*", "faith"),
    ("🕊️", "Is death God's will — or just biology?\n\nBecause if God decides when everyone dies —\n\n*He also decided every genocide, every famine, every child killed in war.*\n\nStill comfortable calling that a plan?", "faith"),
    ("📖", "Hell — eternal torture for a short life. Is that justice or a control mechanism?", "faith"),
     ("🏆", "You worked hard for 10 years and built something.\n\nYou thank God.\n\nBut you did the work. You made the calls. You showed up.\n\n*At what point does the credit belong to you?*", "faith"),
    ("🌅", "Hope is real. Prayer feels real. Community feels real.\n\nBut are those things evidence of God — or evidence that humans need structure and meaning?\n\n*You can have all of those without a deity.*", "faith"),
    ("🛐", "Both Islam and Christianity say only their followers go to heaven. Both can't be right. So?", "faith"),
    ("📖", "Teaching children they are born sinful — is that faith or psychological damage?", "faith"),
     ("🔥", "Hell — eternal torture for rejecting God.\n\nA parent who loved their child unconditionally would never do that.\n\n*Why does God get a pass?*", "faith"),
    ("🔥", "You lived 80 years. You rejected God.\n\nYou burn forever.\n\n*Eternal punishment for a finite life isn't justice. It's sadism.*\n\nDoes that sound like love to you?", "faith"),
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