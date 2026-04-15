"""
daily_broadcast.py — Daily provocative questions to a Telegram channel
Set BROADCAST_CHANNEL in your .env file to your channel username e.g. @teechannel
"""

import os
import random
from dotenv import load_dotenv

load_dotenv()
BROADCAST_CHANNEL = os.getenv("BROADCAST_CHANNEL", "")

DAILY_MESSAGES = [
    ("🔥", "If God already knows you'll go to hell before you're born... why create you at all?", "Think you know the answer? Ask Tee 👇"),
    ("📖", "The Bible has been rewritten over 450 times. Which version is the word of God?", "Tee has thoughts on this 👇"),
    ("🕌", "Muhammad said the sun sets in a muddy spring. He was wrong. What else was he wrong about?", "Ask Tee — no filter 👇"),
    ("💀", "Hell is eternal punishment for a temporary life. That's not justice. That's cruelty.", "Agree or disagree? Tell Tee 👇"),
    ("🧠", "If prayer worked, hospitals would be empty.", "Fight Tee on this 👇"),
    ("👶", "Telling a child they were born sinful is the first act of psychological abuse.", "Hot take or truth? Ask Tee 👇"),
    ("⚔️", "More wars have been fought in God's name than any other cause in history.", "Ask Tee how deep this goes 👇"),
    ("🤡", "Christmas trees, Easter eggs, even the name Easter — all from pagan religions. Christianity borrowed everything.", "Tee will explain 👇"),
    ("💸", "Your pastor is driving a Rolls Royce. Your faith paid for it.", "Tee is not holding back 👇"),
    ("🌍", "Africa is the most religious continent and one of the poorest. Coincidence?", "Tee has a direct answer 👇"),
    ("👁️", "The Council of Nicaea in 325 AD is where humans voted on which parts of the Bible were true.", "Most Christians don't know this. Ask Tee 👇"),
    ("🔬", "Evolution has more evidence than any religion. Yet billions reject it. Why?", "Ask Tee the real reason 👇"),
    ("😤", "Religion gives you invisible enemies (Satan) and invisible heroes (God). Both conveniently unprovable.", "Challenge Tee on this 👇"),
    ("❓", "If God is perfect, why does he need your praise? Insecure gods don't sound very divine.", "Tee is waiting 👇"),
    ("🕊️", "Islam and Christianity both say theirs is the only true path. They can't both be right. So...?", "Ask Tee which one is more wrong 👇"),
]

def get_daily_message() -> tuple:
    emoji, fact, cta = random.choice(DAILY_MESSAGES)
    return emoji, fact, cta

async def broadcast(bot):
    if not BROADCAST_CHANNEL:
        return
    emoji, fact, cta = get_daily_message()
    text = (
        f"{emoji} *Daily Drop*\n\n"
        f"{fact}\n\n"
        f"_{cta}_\n\n"
        f"👉 @your\\_bot\\_username"
    )
    try:
        await bot.send_message(
            chat_id=BROADCAST_CHANNEL,
            text=text,
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Broadcast error: {e}")
