import random

MATRIX_QUESTIONS = [
    # ── LIFE DECISIONS ─────────────────────────────────────────────────────────
    {
        "q": "You wake up tomorrow with 10× your current income.\n\nWhat actually changes in your daily life?",
        "options": [
            ("🏠 I quit my job and relax completely", 1),
            ("✈️ I travel, buy things, enjoy life", 2),
            ("🔨 I invest it and build something bigger", 4),
            ("🤔 Honestly not much — money follows habits", 5),
        ]
    },
    {
        "q": "Most people choose their life path — or drift into it?\n\nWhat do you honestly think?",
        "options": [
            ("✅ Most people choose consciously", 1),
            ("😐 Some choose, most drift", 3),
            ("💀 Most drift — society chooses for them", 5),
            ("🤔 I drifted into mine and I know it", 4),
        ]
    },
    {
        "q": "If you could restart life at age 10 with your current knowledge — would you?",
        "options": [
            ("✅ Absolutely — I'd do everything differently", 3),
            ("😐 Maybe — but I'd make new mistakes anyway", 4),
            ("🤔 I'd change a few things but not everything", 3),
            ("❌ No — the pain shaped who I am", 5),
        ]
    },
    {
        "q": "You have one year left to live and unlimited money.\n\nHow do you spend it?",
        "options": [
            ("🎉 Party, travel, experience everything", 2),
            ("👨‍👩‍👧 Spend it all with family", 3),
            ("🔨 Build something that outlasts me", 5),
            ("😐 I genuinely don't know — that scares me", 4),
        ]
    },
    {
        "q": "Would you rather be respected or comfortable?",
        "options": [
            ("🛋️ Comfortable — peace of mind matters most", 2),
            ("🏆 Respected — legacy matters more than comfort", 4),
            ("😐 Both — why choose?", 2),
            ("💀 Neither — I want to be free", 5),
        ]
    },

    # ── SOCIAL CONDITIONING ────────────────────────────────────────────────────
    {
        "q": "Your parents wanted you to be a doctor or lawyer.\n\nDid their expectations shape what you became?",
        "options": [
            ("✅ Yes — I followed their path", 1),
            ("😐 Partly — I compromised", 2),
            ("💪 No — I chose my own direction", 4),
            ("🔥 I'm still fighting that battle right now", 3),
        ]
    },
    {
        "q": "Most people dress, speak, and act to fit in rather than express themselves.\n\nAre you one of them?",
        "options": [
            ("❌ No — I'm fully authentic", 3),
            ("😬 I'm honest — I care about what people think", 2),
            ("🤔 I filter myself depending on the environment", 3),
            ("💀 Society trained me so well I can't tell the difference", 5),
        ]
    },
    {
        "q": "\"Get a good job, save money, retire at 65.\"\n\nDo you believe that plan still works?",
        "options": [
            ("✅ Yes — stability is the foundation", 1),
            ("😐 It works for most people even if not exciting", 2),
            ("❌ No — that plan was designed for someone else's economy", 4),
            ("💀 That plan assumes you'll be alive and healthy at 65", 5),
        ]
    },
    {
        "q": "If your social media disappeared tomorrow — how would your sense of self change?",
        "options": [
            ("😐 Not much — it's just a tool for me", 4),
            ("😬 I'd feel disconnected from people", 2),
            ("💀 I'd lose my audience and part of my identity", 1),
            ("🔥 I'd probably feel more like myself", 5),
        ]
    },
    {
        "q": "You get an opportunity that pays well but means doing work you hate.\n\nWhat do you do?",
        "options": [
            ("💰 Take it — money solves other problems", 2),
            ("❌ Refuse — I'd rather be poor and fulfilled", 3),
            ("🤔 Take it short-term while building an exit", 5),
            ("😐 Depends on how much — everyone has a price", 2),
        ]
    },

    # ── TIME & PURPOSE ────────────────────────────────────────────────────────
    {
        "q": "How much of your time this week was spent on things YOU chose — versus what others expected of you?",
        "options": [
            ("✅ Most of it was my choice", 4),
            ("😐 About half and half", 3),
            ("😬 Mostly others' demands and expectations", 2),
            ("💀 I'm not sure I've ever truly chosen how I spend time", 1),
        ]
    },
    {
        "q": "The average person spends 7 years of their life watching TV and 6 years on social media.\n\nWhat do you spend your \"extra\" time on?",
        "options": [
            ("📺 Honestly — mostly entertainment", 1),
            ("📚 Learning, reading, or building skills", 5),
            ("💪 Health, family, or real relationships", 4),
            ("🤔 I've never tracked it — maybe I should", 3),
        ]
    },
    {
        "q": "If you knew you'd die in 5 years — would you be living differently right now?",
        "options": [
            ("❌ No — I'm already living intentionally", 5),
            ("😐 A few things would change", 3),
            ("😬 Yes — significantly differently", 2),
            ("💀 Completely differently. This question hurts.", 1),
        ]
    },
    {
        "q": "What does success mean to you — and did you arrive at that definition yourself?",
        "options": [
            ("💰 Money and financial security", 2),
            ("🏆 Achievement and recognition", 2),
            ("🕊️ Freedom and autonomy", 5),
            ("🤔 I'm still figuring out what it means to me", 4),
        ]
    },

    # ── COMFORT VS GROWTH ─────────────────────────────────────────────────────
    {
        "q": "Think of the last time you were deeply uncomfortable.\n\nWere you growing — or just suffering?",
        "options": [
            ("🔥 Growing — discomfort was the teacher", 5),
            ("😢 Just suffering — it didn't lead anywhere", 2),
            ("🤔 I couldn't tell the difference at the time", 3),
            ("😐 I avoid discomfort as much as possible", 1),
        ]
    },
    {
        "q": "Hard work alone leads to success.\n\nDo you believe that?",
        "options": [
            ("✅ Yes — effort always pays off eventually", 2),
            ("😐 Work hard AND work smart — both matter", 3),
            ("❌ No — timing, luck, and networks matter more than people admit", 4),
            ("💀 Hard work is necessary but not sufficient — and most people ignore that", 5),
        ]
    },
    {
        "q": "You can have discipline without motivation — but not motivation without discipline.\n\nAgree?",
        "options": [
            ("❌ No — motivation comes first", 2),
            ("😐 Both work differently for different people", 2),
            ("✅ Yes — discipline is the foundation", 4),
            ("🔥 Motivation is a feeling. Discipline is a decision.", 5),
        ]
    },
    {
        "q": "What is the biggest lie you were told about how life works?",
        "options": [
            ("🏫 \"Study hard and you'll be successful\"", 3),
            ("❤️ \"Follow your passion\"", 4),
            ("🏦 \"The system is fair\"", 5),
            ("😐 I don't think I was lied to significantly", 1),
        ]
    },

    # ── HAPPINESS MYTH ────────────────────────────────────────────────────────
    {
        "q": "Happiness is a destination — something you reach when you achieve enough.\n\nTrue or false?",
        "options": [
            ("✅ True — achieving goals brings lasting happiness", 1),
            ("😐 Partly — achievements help but fade quickly", 3),
            ("❌ False — happiness is a practice not a destination", 5),
            ("🤔 I keep chasing it and it keeps moving", 2),
        ]
    },
    {
        "q": "Most people are unhappy because they don't have enough — or because they want the wrong things?",
        "options": [
            ("💰 Not enough — more resources = more options", 2),
            ("🎯 Wrong things — society sells us desires we didn't choose", 5),
            ("😐 Both are true for different people", 3),
            ("🤔 I'm genuinely unsure which applies to me", 3),
        ]
    },

    # ── SURVIVAL & INSTINCT ───────────────────────────────────────────────────
    {
        "q": "In a real crisis — job loss, health collapse, relationship ending — what is your first instinct?",
        "options": [
            ("🧠 Analyse the situation and make a plan", 5),
            ("📞 Call someone for support", 3),
            ("😶 Freeze and wait for clarity", 2),
            ("😤 React emotionally first — logic comes later", 1),
        ]
    },
    {
        "q": "Your friend group is heading in a direction that doesn't align with your goals.\n\nWhat do you do?",
        "options": [
            ("👋 Gradually distance yourself — environments shape you", 5),
            ("😐 Stay but protect your energy", 3),
            ("💬 Try to influence them toward better directions", 4),
            ("🤷 Do nothing — loyalty matters more than growth", 1),
        ]
    },
    {
        "q": "The pain of staying the same vs the pain of changing.\n\nWhich pain do you choose more often?",
        "options": [
            ("🔥 Pain of change — I push myself", 5),
            ("😐 It depends on how big the change is", 3),
            ("😬 Pain of staying — change feels too risky", 1),
            ("💀 I didn't realise I was choosing until now", 2),
        ]
    },
    {
        "q": "You discover your closest friend has been lying to you for years — not maliciously, but to protect you.\n\nHow do you respond?",
        "options": [
            ("😤 Hurt but I understand — I'd move forward", 3),
            ("❌ Trust broken — I need space", 2),
            ("🤔 I'd evaluate whether I preferred the lie", 4),
            ("💡 This makes me question what else I believe is true", 5),
        ]
    },

    # ── THE BECOMING ─────────────────────────────────────────────────────────
    {
        "q": "\"Becoming yourself\" is painful because it requires disappointing people who needed you to stay the same.\n\nHave you experienced that?",
        "options": [
            ("✅ Yes — deeply. It's the hardest thing I've done", 5),
            ("😐 Somewhat — I've outgrown some relationships", 4),
            ("😬 I avoid it — I don't want to hurt people", 2),
            ("🤔 I'm still figuring out who I'm becoming", 3),
        ]
    },
    {
        "q": "What version of yourself are you most afraid other people will find out about?",
        "options": [
            ("😐 The insecure one", 3),
            ("😬 The one who doesn't have it figured out", 3),
            ("💀 The one who settled for less than I'm capable of", 4),
            ("🔥 I've made peace with all my versions", 5),
        ]
    },
    {
        "q": "Most people know what they need to do to improve their life.\n\nThey just don't do it. Why?",
        "options": [
            ("😤 Fear of failure", 3),
            ("🛋️ Comfort is too easy to choose", 4),
            ("👥 They need the right environment and support", 3),
            ("💀 They secretly don't believe they deserve better", 5),
        ]
    },

    # ── WEALTH & MONEY MYTHS ──────────────────────────────────────────────────
    {
        "q": "Most people want to be rich. But if you got 10x richer tomorrow — what would actually be different about you as a person?",
        "options": [
            ("😐 I'd be happier and less stressed", 1),
            ("💪 I'd have more freedom to be myself", 3),
            ("🤔 Honestly not much — money reveals character, doesn't create it", 5),
            ("💰 Everything would change — money changes everything", 2),
        ]
    },
    {
        "q": "Rich people work hard. But so do poor people. What actually separates them?",
        "options": [
            ("💪 Work ethic and discipline", 2),
            ("🎓 Education and skills", 2),
            ("♟️ Access, timing, and who they know", 5),
            ("🍀 Mostly luck if we're honest", 3),
        ]
    },
    {
        "q": "You get a $500k windfall tomorrow. What's your first move?",
        "options": [
            ("🏠 Buy a house or car", 1),
            ("✈️ Travel and enjoy life first", 2),
            ("📈 Invest it and live off the returns", 5),
            ("💸 Pay off debts and save the rest", 3),
        ]
    },
    {
        "q": "Most people's relationship with money is based on what their parents taught them. Did your parents have a healthy relationship with money?",
        "options": [
            ("✅ Yes — they were great examples", 3),
            ("😐 Average — neither great nor terrible", 2),
            ("😬 No — and I've had to unlearn a lot", 5),
            ("🤔 I never thought about where my money beliefs came from", 1),
        ]
    },
    {
        "q": "Status spending — buying things to signal success — accounts for how much of your monthly spend?",
        "options": [
            ("✅ Almost none — I buy what I need", 4),
            ("😐 Some — I like nice things", 3),
            ("😬 More than I'd like to admit", 2),
            ("💀 I haven't tracked it but the question makes me uncomfortable", 1),
        ]
    },

    # ── RELATIONSHIPS & SOCIAL DYNAMICS ──────────────────────────────────────
    {
        "q": "You are the average of your 5 closest friends. Do you like who that average makes you?",
        "options": [
            ("✅ Yes — I'm surrounded by people who push me", 5),
            ("😐 Some of them lift me, some hold me back", 3),
            ("😬 Honestly — no. I've outgrown most of them", 4),
            ("🤔 I never thought about it that way", 2),
        ]
    },
    {
        "q": "Most conflicts in relationships are really about unspoken expectations. Do you agree?",
        "options": [
            ("✅ Yes — expectations kill more relationships than cheating does", 5),
            ("😐 Partly — but some people are just difficult", 3),
            ("❌ No — conflict is usually about real incompatibility", 2),
            ("🤔 I don't know — I avoid conflict", 1),
        ]
    },
    {
        "q": "You find out a close friend has been subtly undermining you to mutual friends for years. How do you respond?",
        "options": [
            ("😤 Confront them directly and cut ties if needed", 5),
            ("😐 Distance myself quietly without confrontation", 3),
            ("😢 Try to fix it — I value the relationship", 2),
            ("🤔 Question what I did to cause it", 1),
        ]
    },
    {
        "q": "Loneliness is one of the biggest epidemics of our time. Are you lonely — even when surrounded by people?",
        "options": [
            ("❌ No — my connections feel genuine", 5),
            ("😐 Sometimes — surface-level connections everywhere", 3),
            ("😢 Yes — often", 2),
            ("💀 I'm not sure I've allowed myself to know", 1),
        ]
    },
    {
        "q": "How much of your self-worth depends on what others think of you?",
        "options": [
            ("✅ Almost none — I know my own value", 5),
            ("😐 Some — I care but I don't obsess", 3),
            ("😬 More than I should — I'm working on it", 2),
            ("💀 Most of it — and that scares me", 1),
        ]
    },

    # ── FEAR & COMFORT ZONE ───────────────────────────────────────────────────
    {
        "q": "What is the one thing you know you should do but keep finding reasons not to?",
        "options": [
            ("📣 Put myself out there more — start the thing", 3),
            ("💪 Get physically healthy — exercise, diet", 3),
            ("💼 Leave the job / relationship / city that's holding me back", 4),
            ("✅ I'm actually doing it — no excuses right now", 5),
        ]
    },
    {
        "q": "Fear of failure vs fear of success — which one actually holds you back more?",
        "options": [
            ("😰 Fear of failure — I'm scared of losing", 3),
            ("👀 Fear of success — I'm scared of what changes if I win", 5),
            ("😐 Both equally", 2),
            ("💪 Neither — I move despite fear", 5),
        ]
    },
    {
        "q": "When was the last time you did something that genuinely scared you?",
        "options": [
            ("🔥 Recently — I push myself regularly", 5),
            ("😐 A while ago — maybe a year", 3),
            ("😬 I can't remember — I've been very comfortable", 1),
            ("💀 I avoid things that scare me by design", 1),
        ]
    },
    {
        "q": "Comfort is the enemy of growth. Do you live by that — or just agree with it intellectually?",
        "options": [
            ("✅ I live by it — I choose discomfort deliberately", 5),
            ("😐 I try but comfort wins more than I'd like", 3),
            ("📖 I agree with it but mostly in theory", 2),
            ("❌ I disagree — comfort allows consistency", 1),
        ]
    },
    {
        "q": "You get offered a role that's 50% above your current salary but requires you to be fully uncomfortable for at least 2 years. Do you take it?",
        "options": [
            ("✅ Yes immediately — discomfort is the price of growth", 5),
            ("🤔 Depends on what kind of uncomfortable", 3),
            ("😬 Probably not — stability matters more right now", 2),
            ("❌ No — I value peace over money", 1),
        ]
    },

    # ── LONG-TERM THINKING ────────────────────────────────────────────────────
    {
        "q": "Where do you want to be in 10 years? Can you describe it in specific detail right now?",
        "options": [
            ("✅ Yes — I have a clear specific vision", 5),
            ("😐 General idea — not specific", 3),
            ("😬 Vague feelings — nothing concrete", 2),
            ("💀 I avoid thinking about it — it makes me anxious", 1),
        ]
    },
    {
        "q": "Most people overestimate what they can do in one year and underestimate what they can do in ten. Do you think in decades?",
        "options": [
            ("✅ Yes — I make decisions with 10-year consequences in mind", 5),
            ("😐 I try to — but I mostly think in months", 3),
            ("❌ I mostly think week to week", 2),
            ("🤔 I never thought about thinking in decades", 1),
        ]
    },
    {
        "q": "Delayed gratification — giving up something now for something bigger later. Rate yourself honestly 1-10.",
        "options": [
            ("🔥 8-10 — I consistently choose long-term", 5),
            ("😐 5-7 — I'm working on it", 3),
            ("😬 3-4 — I struggle with it", 2),
            ("💀 1-2 — I live very much in the present", 1),
        ]
    },
    {
        "q": "What decision from 5 years ago are you still paying for today?",
        "options": [
            ("✅ None I can think of — I made good calls", 4),
            ("😐 One or two small ones", 3),
            ("😬 A major one that still affects me daily", 2),
            ("💀 I try not to think about it", 1),
        ]
    },
    {
        "q": "Are you building an asset or trading your time for money?",
        "options": [
            ("🏗️ Building an asset — something that grows without me", 5),
            ("😐 Both — I'm transitioning", 4),
            ("⏰ Mostly trading time — but I know I need to change", 2),
            ("💰 Trading time — and I'm fine with it for now", 1),
        ]
    },

    # ── IDENTITY & AUTHENTICITY ───────────────────────────────────────────────
    {
        "q": "If you removed your job title, your relationships, and your possessions — who are you?",
        "options": [
            ("✅ I know exactly who I am without those things", 5),
            ("😐 I have some sense of self beyond them", 3),
            ("😬 That question genuinely unsettles me", 2),
            ("💀 I haven't separated myself from those things in my mind", 1),
        ]
    },
    {
        "q": "How much of your personality is authentically yours vs shaped by the culture, family, and environment you grew up in?",
        "options": [
            ("✅ Mostly mine — I've done the work to separate", 5),
            ("😐 Mixed — some authentic, some inherited", 3),
            ("😬 Mostly inherited — I'm only beginning to question it", 2),
            ("💀 I can't tell the difference and that's the problem", 1),
        ]
    },
    {
        "q": "What would you do differently if nobody you knew would ever find out?",
        "options": [
            ("✅ Nothing — I live consistently regardless of observers", 5),
            ("😐 A few small things", 3),
            ("😬 Quite a bit actually", 2),
            ("💀 This question reveals how much I perform for others", 1),
        ]
    },
    {
        "q": "The version of you that you show on social media vs who you are alone at 2am. How different are they?",
        "options": [
            ("✅ Almost identical — I'm consistent", 5),
            ("😐 Some gap — I show my best self online", 3),
            ("😬 Very different — they barely know me", 2),
            ("💀 The 2am version would embarrass the public version", 1),
        ]
    },
    {
        "q": "Have you ever made a major life decision just to meet someone else's expectations — and regretted it?",
        "options": [
            ("❌ No — I've always chosen for myself", 4),
            ("😐 Once or twice — minor things", 3),
            ("😬 Yes — a significant one I'm still dealing with", 2),
            ("💀 Most of my major decisions were shaped by others' expectations", 1),
        ]
    },

    # ── DISCIPLINE & EXECUTION ────────────────────────────────────────────────
    {
        "q": "What is the biggest gap between what you know you should do and what you actually do?",
        "options": [
            ("💪 Health — I know but don't act", 2),
            ("💰 Money — I know the principles but don't apply them", 2),
            ("📣 Putting myself out there — I know I should but fear stops me", 3),
            ("✅ The gap is small — I generally do what I know", 5),
        ]
    },
    {
        "q": "How many times have you started something meaningful and not finished it in the last 2 years?",
        "options": [
            ("✅ None — I finish what I start", 5),
            ("😐 1-2 times", 3),
            ("😬 3-5 times", 2),
            ("💀 More than 5 — I'm a great starter and a poor finisher", 1),
        ]
    },
    {
        "q": "Motivation gets you started. Discipline keeps you going. Which one do you have more of?",
        "options": [
            ("🔥 Discipline — I show up regardless of how I feel", 5),
            ("✨ Motivation — when I'm fired up I'm unstoppable", 2),
            ("😐 Neither consistently", 1),
            ("🤔 I've been confusing the two my whole life", 3),
        ]
    },
    {
        "q": "What habit, if you built it and kept it for one year, would change your life the most?",
        "options": [
            ("📚 Learning something new every day", 4),
            ("💪 Consistent exercise", 3),
            ("💰 Saving and investing a fixed percentage of income", 4),
            ("🤔 I know what it is but I haven't started yet", 2),
        ]
    },
    {
        "q": "Your environment shapes your behaviour more than your willpower does. Have you designed your environment to support who you want to become?",
        "options": [
            ("✅ Yes — deliberately and intentionally", 5),
            ("😐 Somewhat — some things are set up right", 3),
            ("❌ No — I rely on willpower and wonder why I keep failing", 1),
            ("🤔 I never thought about designing my environment", 2),
        ]
    },

    # ── AFRICA & SOCIETY ──────────────────────────────────────────────────────
    {
        "q": "Africa has the youngest population in the world and some of the most resources. Yet it remains the poorest continent. What is the real reason?",
        "options": [
            ("🌍 Colonial legacy and continued exploitation", 4),
            ("👨‍👩‍👧 Leadership failure and corruption", 3),
            ("🧠 Mindset — we've been conditioned to build for others not ourselves", 5),
            ("😐 It's complicated — no single cause", 3),
        ]
    },
    {
        "q": "A young African who grows up believing success means leaving Africa and working abroad — is that ambition or conditioning?",
        "options": [
            ("✈️ Ambition — go where the opportunity is", 2),
            ("💀 Conditioning — taught to see home as a problem to escape", 5),
            ("😐 Both — practical and also partly conditioned", 4),
            ("🤔 I've never questioned that assumption", 1),
        ]
    },
    {
        "q": "Social media shows the 1% of African success stories while hiding the systemic traps. Has it changed how you see your own potential?",
        "options": [
            ("✅ It inspires me — proof that it's possible", 3),
            ("😐 I'm aware it's curated but still influenced by it", 3),
            ("🧠 I use it as data — not as a measure of my own progress", 5),
            ("💀 It has made me feel behind in ways that aren't real", 1),
        ]
    },
    {
        "q": "The hustle culture narrative says work 18 hours a day and you'll make it. Is that wisdom or exploitation dressed as motivation?",
        "options": [
            ("💪 Wisdom — hard work is non-negotiable", 2),
            ("💀 Exploitation — keeping workers productive while owners profit", 5),
            ("😐 Somewhere in between", 3),
            ("🤔 I've lived it and I'm not sure it worked", 2),
        ]
    },

    # ── DEEP TRUTH ────────────────────────────────────────────────────────────
    {
        "q": "If you could read the honest, unfiltered thoughts your 5 closest people have about you — would you want to?",
        "options": [
            ("✅ Yes — I can handle the truth", 5),
            ("😐 Most of it yes — some of it no", 3),
            ("😬 No — I'd rather not know", 2),
            ("💀 I avoid situations where my self-image might be challenged", 1),
        ]
    },
    {
        "q": "What story do you keep telling yourself that is almost certainly not true?",
        "options": [
            ("😐 That I'll start when conditions are perfect", 2),
            ("😬 That I'm not ready yet", 2),
            ("💀 That I'm different from others and the normal rules don't apply to me", 3),
            ("✅ I've identified my stories and I challenge them actively", 5),
        ]
    },
    {
        "q": "The most dangerous prison is the one you can't see. What invisible prison might you be in right now?",
        "options": [
            ("👥 Other people's opinions of me", 2),
            ("🏦 Financial obligations that limit my choices", 3),
            ("🧠 My own beliefs about what I'm capable of", 4),
            ("✅ I don't think I'm in one — I feel genuinely free", 5),
        ]
    },
    {
        "q": "On a scale of honesty — how much of your current life did you consciously choose vs slide into?",
        "options": [
            ("✅ Mostly chose — I've been intentional", 5),
            ("😐 About half and half", 3),
            ("😬 Mostly slid into — circumstances led, I followed", 2),
            ("💀 Almost entirely slid — I'm only now waking up to it", 1),
        ]
    },
    {
        "q": "What would the most honest version of you say to the version of you that is answering these questions?",
        "options": [
            ("✅ You're doing well — keep going", 4),
            ("😤 Stop pretending you have it figured out", 3),
            ("💀 You know what needs to change — stop delaying it", 5),
            ("😐 You're closer than you think but not as close as you believe", 4),
        ]
    },
]

def get_matrix_questions(n=20):
    return random.sample(MATRIX_QUESTIONS, min(n, len(MATRIX_QUESTIONS))) 