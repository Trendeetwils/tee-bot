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
    # Add these to DAILY_DROPS:
    # Prayer (Theme 47)
    ("🙏", "If God already has a plan — what exactly is prayer changing?\n\nYou're asking an all-knowing God to reconsider.\n\n*That's not faith. That's lobbying.*", "faith"),
    ("🙏", "Rudy Giuliani left the ICU.\n\nHis team credited prayer — not the doctors.\n\nIf prayer saved him — why did he need the ICU in the first place?\n\n*You don't get to use both and credit only one.*", "faith"),
    ("🙏", "'I'm praying for you' after a tragedy is the socially acceptable way of saying 'I'm doing nothing.'\n\nAnd somehow — *that's considered kind.*", "faith"),

    # Aisha (Theme 26)
    ("📖", "Muhammad married Aisha when she was 6. Consummated when she was 9.\n\nThe defence: 'It was normal back then.'\n\nSo was slavery. Does 'normal back then' make it right?", "faith"),
    ("📖", "If a man today said God told him to marry a 9-year-old — he'd be in prison.\n\nIn the 7th century — he became the most followed prophet in history.\n\n*Context doesn't make it less wrong. It makes us ask harder questions.*", "faith"),

    # Four wives (Theme 27)
    ("📖", "Islam allows men up to 4 wives.\n\nWomen get 1 husband.\n\nIf God designed marriage — why did he design it so differently for men and women?\n\n*Unless it wasn't God who designed it.*", "faith"),

    # Sunk cost (Theme 37)
    ("🎰", "40 years of prayer. Decades of tithing. A lifetime of faith.\n\nAnd now you're too invested to question it.\n\n*That's not devotion. That's a sunk cost.*", "faith"),
    ("🎰", "Most people stay religious for the same reason people stay in bad relationships.\n\n*They've put in too much to walk away.*\n\nIs that faith — or fear of wasted time?", "faith"),

    # Pascal's Wager (Theme 38)
    ("🎲", "'Believe just in case — you have nothing to lose.'\n\nExcept: which of the 4,000 gods do you bet on?\n\nBelieving in the wrong one might be worse than none.\n\n*Pascal's wager only works if there's one option.*", "faith"),

    # Religious trauma (Theme 52)
    ("🧠", "Telling a 5-year-old they are born sinful and deserve hell — repeated every Sunday for 18 years.\n\n*We call that upbringing. Therapists call it something else.*", "faith"),
    ("🧠", "Imagine a partner who said: 'Don't trust your heart — it is deceitful and wicked.'\n\nWe'd call that emotional abuse.\n\nWhen religion says it to a child — we call it theology.", "faith"),
    ("🧠", "Religious trauma doesn't always look like visible wounds.\n\nSometimes it's a 30-year-old who still can't make decisions without guilt.\n\n*The church they left decades ago still lives in their head.*", "faith"),

    # Bible/Quran assembly (Theme 53)
    ("📖", "The Bible's canon was decided by a committee vote in 397 AD.\n\nBooks were included. Books were excluded.\n\n*Humans voted on the word of God.*\n\nComfortable with that?", "faith"),
    ("📖", "The Gospel of Mark was written 40 years after Jesus died.\n\nMatthew and Luke copied from it — word for word in places.\n\n*Four independent eyewitnesses don't copy each other.*", "faith"),
    ("📖", "Uthman — the 3rd Caliph — standardized the Quran and ordered all other versions burned.\n\nWe will never know what those versions said.\n\n*The word of God — decided by a politician.*", "faith"),
    ("📖", "Abraham riding a camel sounds harmless.\n\nExcept camels weren't domesticated in that region until 1,000 years after Abraham supposedly lived.\n\n*The author was writing from their own time. Into the past.*", "faith"),

    # Evolution (Theme 50)
    ("🧬", "'Evolution is just a theory.'\n\nSo is gravity.\n\nIn science, theory doesn't mean guess — it means the best explanation supported by mountains of evidence.\n\n*Try jumping off a building and test both theories simultaneously.*", "faith"),
    ("🧬", "Creationists accept micro-evolution — small changes within species.\n\nBut reject macro-evolution — big changes over millions of years.\n\nThat's like believing in stairs but not staircases.\n\n*It's the same mechanism. Just more time.*", "faith"),

    # Science self-corrects (Theme 51)
    ("🔬", "Religion calls it a weakness that science keeps changing.\n\nScientists call it the whole point.\n\n*A map that updates when new roads are built is more useful than one that insists the roads haven't changed since 700 AD.*", "faith"),

    # Spiritual not religious (Theme 48)
    ("✨", "'I'm not religious — I'm spiritual.'\n\nTranslation: I left the cage but I still like the smell of the bars.\n\n*Spirituality without evidence is just religion with better branding.*", "faith"),
    ("✨", "Crystals, chakras, manifesting, moon water.\n\nPeople left organized religion to escape magical thinking.\n\n*Then bought magical thinking with a better aesthetic.*", "faith"),

    # Meaning question (Theme 49)
    ("🌌", "Religion's answer to 'why do we exist?'\n\nTo serve God.\n\nYou are born. You suffer. You die.\n\nAnd the whole point was to praise the being who designed the suffering.\n\n*That's not meaning. That's a job you never applied for.*", "faith"),
    ("🌌", "'What's the point without God?'\n\nAsks God to be an answer — but God is just another question.\n\nWhat's God's point? Who gave him purpose?\n\n*You haven't solved the problem. You've outsourced it.*", "matrix"),

    # Osho/spiritual leaders (Theme 36)
    ("👁️", "Osho had Rolls Royces, a commune of followers, and claimed enlightenment.\n\nHe was eventually deported for fraud and immigration violations.\n\n*The only thing distinguishing him from a prophet is time.*", "faith"),
    ("👁️", "Every religious leader in history has said the same thing:\n\n'God speaks to me. Not to you. Through me.'\n\n*At what point does that stop being divine revelation and start being a business model?*", "faith"),

    # Mutual exclusivity (Theme 46)  
    ("🛐", "Christianity and Islam both say only their followers reach heaven.\n\nBoth cannot be right.\n\nOne is wrong about the most important question in their theology.\n\n*Which one — and how do you know?*", "faith"),
    # Prosperity Gospel / Televangelists
    ("💸", "Joel Osteen preaches that faith brings wealth.\n\nHe lives in a $10 million mansion.\n\nHis congregation doesn't.\n\n*The only prosperity gospel that works is the one where you're the one selling it.*", "faith"),

    ("💸", "Give money to the church, God gives it back tenfold.\n\nIf it doesn't work — you didn't have enough faith.\n\nIf it does work — God is good.\n\n*The preacher wins either way. You cannot falsify this. That's not theology. That's a pyramid scheme.*", "faith"),

    ("✈️", "Kenneth Copeland asked his congregation why he needs a private jet.\n\nHis answer: so he doesn't have to fly in a tube with 'a bunch of demons.'\n\nHe has multiple jets.\n\n*Your tithe bought one of them.*", "faith"),

    ("🏟️", "Joel Osteen's church is a former NBA arena.\nSeating: 16,000.\nWhen Hurricane Harvey flooded Houston — he initially refused to open it as a shelter.\n\n*They opened it after the backlash. Not after the flood.*", "faith"),

    ("💸", "Prosperity gospel spreads fastest in the world's poorest communities.\n\nPeople who can't afford food give their savings to a pastor promising God will multiply it.\n\n*The pastor builds a mansion. The congregation stays poor. And then gets told they didn't have enough faith.*", "faith"),

    ("💸", "Creflo Dollar asked his congregation to crowdfund a $65 million private jet.\n\nHe said he needed it to spread the gospel.\n\nJesus walked.\n\n*Something changed in the translation.*", "faith"),
    
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