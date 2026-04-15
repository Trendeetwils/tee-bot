import random

ALL_QUESTIONS = [

    # ── CORE BELIEF ────────────────────────────────────────────────────────────
    {
        "q": "Children are suffering everywhere. Wars. Disease. Famine.\n\nWhat do you think?",
        "options": [("🙏 God has a plan we don't understand", 0), ("📖 He is testing us", 1), ("🤷 He exists but doesn't care", 3), ("💀 No loving God allows this", 5)]
    },
    {
        "q": "The Bible and Quran — what are they?",
        "options": [("✅ Word of God, fully true", 0), ("🖊️ Inspired by God, written by humans", 1), ("📚 Historical book, some good lessons", 3), ("❌ Man-made myths and contradictions", 5)]
    },
    {
        "q": "Do you pray?",
        "options": [("✅ Every day — it works", 0), ("😐 Sometimes, more out of habit", 2), ("🤔 Rarely — I doubt it changes anything", 4), ("🚫 Never — nobody is listening", 5)]
    },
    {
        "q": "What do you think about Hell?",
        "options": [("😰 It's real — reject God and you go there", 0), ("🌫️ More symbolic than a real place", 2), ("❓ Eternal punishment for a short life makes no sense", 4), ("🎭 A fear tactic invented to control people", 5)]
    },
    {
        "q": "Is there ANY chance God exists?",
        "options": [("✅ 100% — I have no doubt", 0), ("😐 Probably yes but I have questions", 2), ("🤔 Very unlikely but I can't be 100% sure", 4), ("❌ No — the evidence points to no God", 5)]
    },
    {
        "q": "Can someone be moral without believing in God?",
        "options": [("❌ No — morality comes from God", 0), ("😬 It's harder but possible", 2), ("✅ Yes — most non-religious people are decent", 4), ("💯 Religion has nothing to do with being good", 5)]
    },
    {
        "q": "If your child told you they were atheist — how would you feel?",
        "options": [("😰 Heartbroken — I'd pray for them", 0), ("😬 Worried but I'd still love them", 2), ("😐 Surprised but I'd respect their choice", 3), ("✅ Proud — they're thinking for themselves", 5)]
    },
    {
        "q": "God knew you'd sin before you were born yet plans to punish you. Is that fair?",
        "options": [("✅ His ways are higher than ours", 0), ("🤷 It's a mystery I accept by faith", 1), ("😐 That logic has always bothered me", 4), ("❌ That's not justice — that's a setup", 5)]
    },
    {
        "q": "If God is everywhere and sees everything — why does he need your worship?",
        "options": [("🙏 Worship is for our benefit not his", 0), ("🤔 I've never fully understood that", 2), ("😐 It does feel strange when you think about it", 4), ("🤡 Sounds like a very insecure God", 5)]
    },
    {
        "q": "What happens when you die?",
        "options": [("😇 Heaven or Hell based on your faith", 0), ("🔄 Some kind of afterlife or reincarnation", 2), ("🤷 Nobody really knows", 3), ("🖤 Nothing — consciousness ends. That's okay.", 5)]
    },

    # ── ISLAM SPECIFIC ─────────────────────────────────────────────────────────
    {
        "q": "Muhammad marrying a 9-year-old — your honest reaction?",
        "options": [("✅ Different times, different rules", 0), ("😬 Uncomfortable but I leave it to scholars", 1), ("❌ No moral God would approve this", 4), ("💀 This alone disqualifies the religion for me", 5)]
    },
    {
        "q": "The Quran says the sun sets in a muddy spring (18:86). Your take?",
        "options": [("✅ It has a deeper spiritual meaning", 0), ("🤔 Describing what the traveller saw", 1), ("😬 That's clearly a scientific error", 4), ("💀 A God who wrote this didn't make the universe", 5)]
    },
    {
        "q": "Blasphemy laws — insulting religion can get you killed in some countries. Your take?",
        "options": [("✅ Sacred things deserve legal protection", 0), ("😬 Too extreme but I understand the intent", 1), ("❌ No idea deserves protection from criticism", 4), ("🔥 Proof religion can't survive honest questions", 5)]
    },
    {
        "q": "The Quran allows men to beat their wives (4:34). How does that sit with you?",
        "options": [("✅ In context it means light correction", 0), ("😬 Scholars debate what it really means", 1), ("❌ No loving God would ever write that", 4), ("💀 That verse alone proves it's a man-made book", 5)]
    },
    {
        "q": "Apostasy — leaving Islam — can carry the death penalty in some countries. Your view?",
        "options": [("✅ Faith must be protected from corruption", 0), ("😐 Extreme but it's their law", 1), ("❌ No one should die for changing their mind", 4), ("🔥 If your religion needs death threats to keep people — it's a prison", 5)]
    },
    {
        "q": "Islam spread across Africa and the Middle East largely by conquest. Does that matter?",
        "options": [("🙏 God uses all means to spread truth", 0), ("😐 Most religions spread through power", 2), ("😤 A religion of peace shouldn't spread by the sword", 4), ("💀 Forced conversion is just colonialism with a prayer mat", 5)]
    },

    # ── CHRISTIANITY SPECIFIC ──────────────────────────────────────────────────
    {
        "q": "The Trinity — Father, Son and Holy Spirit are one God. Does that make sense?",
        "options": [("✅ Yes, it's a holy mystery", 0), ("🤔 I accept it by faith even if confusing", 1), ("😐 It's contradictory but I stay in the faith", 3), ("🤡 No — one is one, not three", 5)]
    },
    {
        "q": "The Bible has been translated and rewritten over 450 times. Which version is the real word of God?",
        "options": [("✅ The core message stays the same", 0), ("😐 The original manuscripts are what matters", 1), ("🤔 That's a question I've struggled with honestly", 3), ("💀 If God wrote it why did humans need to keep rewriting it", 5)]
    },
    {
        "q": "Original sin — all humans born guilty because of Adam and Eve. Fair?",
        "options": [("✅ Yes — we inherited a fallen nature", 0), ("😐 It's more symbolic than literal", 2), ("❌ Punishing all of humanity for one act is unjust", 4), ("💀 No moral legal system punishes children for their parents", 5)]
    },
    {
        "q": "Christmas trees, Easter eggs, the name Easter — all from pagan traditions. Does that change anything?",
        "options": [("🙏 We gave them Christian meaning", 0), ("😐 Interesting but doesn't shake my faith", 1), ("🤔 Shows Christianity absorbed older religions", 3), ("💀 Christianity was built on borrowed myths", 5)]
    },
    {
        "q": "The Bible approves of slavery in multiple verses. Your take?",
        "options": [("✅ Different era — God allowed it then", 0), ("😬 It was cultural not divine instruction", 2), ("❌ A moral God would never approve slavery", 4), ("💀 This alone proves the Bible is man-made", 5)]
    },
    {
        "q": "The Council of Nicaea in 325 AD is where humans voted on which parts of the Bible were true. Does that concern you?",
        "options": [("🙏 God guided those decisions", 0), ("😐 Humans were instruments of God's will", 1), ("🤔 It does raise questions about what was left out", 4), ("💀 So the word of God was decided by a committee vote", 5)]
    },

    # ── SCIENCE VS RELIGION ────────────────────────────────────────────────────
    {
        "q": "Science says the universe is 13.8 billion years old. Genesis says it was created in 6 days. Who's right?",
        "options": [("✅ Genesis — God's word over science", 0), ("😐 The 6 days are symbolic not literal", 2), ("🔬 Science clearly — evidence wins", 4), ("💀 The math alone proves the Bible is not literal history", 5)]
    },
    {
        "q": "The Big Bang theory explains the origin of the universe with evidence. Does that leave room for God?",
        "options": [("✅ God triggered the Big Bang", 0), ("🤷 Maybe something existed before the Bang", 2), ("🔬 The Big Bang needs no creator to work", 4), ("💀 The universe can come from quantum fluctuation — no God needed", 5)]
    },
    {
        "q": "Evolution is supported by fossils, DNA, and observation. Do you accept it?",
        "options": [("❌ I reject it — God created us", 0), ("🌱 God used evolution as his tool", 2), ("🤷 I accept it but still wonder about a creator", 3), ("✅ Evolution is fact — no God needed", 5)]
    },
    {
        "q": "The human genome shows we share 98.7% DNA with chimpanzees. What does that tell you?",
        "options": [("🙏 God used similar designs — it means nothing", 0), ("😐 Interesting but not proof of evolution", 1), ("🧬 We clearly share a common ancestor", 4), ("💀 We ARE primates — the Bible got the origin story wrong", 5)]
    },
    {
        "q": "Neuroscience can now trigger religious experiences by stimulating the brain. What does that mean?",
        "options": [("🙏 God works through the brain he designed", 0), ("🤷 It's one explanation among many", 2), ("🧠 Religious experiences are brain events not divine contact", 4), ("💀 God is a neurological phenomenon not a real being", 5)]
    },
    {
        "q": "The universe has 2 trillion galaxies each with billions of stars. Did God make all of that just for humans on one planet?",
        "options": [("✅ Yes — humans are the crown of creation", 0), ("😐 Maybe there are other beings elsewhere", 2), ("🤔 That scale makes human-centred religion feel very small", 4), ("💀 The universe is indifferent — there's no crown of creation", 5)]
    },
    {
        "q": "Carbon dating confirms the Earth is 4.5 billion years old. Genesis says a few thousand years. How do you reconcile that?",
        "options": [("✅ Carbon dating has flaws — I trust scripture", 0), ("😐 Genesis is poetry not science", 2), ("🔬 Science uses multiple methods that all agree", 4), ("💀 Young earth creationism is scientifically impossible", 5)]
    },
    {
        "q": "Antibiotics stop working when bacteria evolve resistance. We see evolution happening in real time. Does that change anything for you?",
        "options": [("🙏 God designed bacteria to adapt", 0), ("😐 Micro evolution yes — human origins no", 2), ("🧬 This is evolution — the same process that shaped us", 4), ("💀 Real-time evolution is proof — not theory", 5)]
    },
    {
        "q": "The same prayer study done with proper controls shows prayer has zero statistical effect on outcomes. Your response?",
        "options": [("🙏 God can't be tested by science", 0), ("😐 Faith isn't about statistical proof", 2), ("🧠 If prayer worked we'd see it in data", 4), ("💀 Hospitals would be empty if prayer worked", 5)]
    },
    {
        "q": "Science has explained the origin of stars, planets, life, and consciousness. What is left for God to explain?",
        "options": [("✅ Everything — God works through science", 0), ("🌌 The things science hasn't reached yet", 2), ("😬 Less and less honestly", 4), ("❌ Nothing that science doesn't already explain better", 5)]
    },

    # ── ARCHAEOLOGY & HISTORY ──────────────────────────────────────────────────
    {
        "q": "Archaeologists have found zero evidence of the Exodus — no camps, no graves, no Egyptian records. Your take?",
        "options": [("🙏 Absence of evidence isn't evidence of absence", 0), ("😐 Ancient records weren't always kept", 1), ("🤔 It raises real questions about biblical history", 4), ("💀 400 years of 2 million people left no trace because it didn't happen", 5)]
    },
    {
        "q": "The walls of Jericho were destroyed 150 years before Joshua's army supposedly arrived. Your response?",
        "options": [("🙏 Dating methods have margin of error", 0), ("😐 The story may be symbolic", 1), ("🤔 That's a significant historical problem", 4), ("💀 The Bible consistently fails the archaeology test", 5)]
    },
    {
        "q": "Most historians agree Jesus existed as a historical figure but reject the resurrection as a physical event. Where do you stand?",
        "options": [("✅ Jesus rose physically — I believe it fully", 0), ("😐 Historical Jesus yes — resurrection is faith not history", 2), ("🤔 The accounts were written 40-70 years after his death — reliability?", 4), ("💀 The resurrection story follows the same pattern as older dying-god myths", 5)]
    },
    {
        "q": "The story of Noah's flood mirrors the much older Babylonian Epic of Gilgamesh almost exactly. Coincidence?",
        "options": [("🙏 The same flood happened — different cultures recorded it", 0), ("😐 Shared cultural memory of a real flood", 1), ("🤔 The Bible clearly borrowed this story from Babylon", 4), ("💀 Biblical stories are recycled mythology from older civilisations", 5)]
    },
    {
        "q": "Egyptian records show no record of Joseph as prime minister or Moses. How do you explain that?",
        "options": [("🙏 God preserved the truth in scripture alone", 0), ("😐 Egypt wouldn't record their own humiliation", 1), ("🤔 These are serious historical gaps", 4), ("💀 These events didn't happen outside of the text that claimed they did", 5)]
    },
    {
        "q": "The Dead Sea Scrolls show the Bible changed significantly over time. Key prophecies about Jesus were added centuries later. Your reaction?",
        "options": [("🙏 God protected the core message", 0), ("😐 Minor changes don't affect the truth", 1), ("🤔 Retroactive prophecy should concern every believer", 4), ("💀 If God wrote it — why did humans need to edit the prophecies?", 5)]
    },

    # ── SCIENTOLOGY & OTHER RELIGIONS ─────────────────────────────────────────
    {
        "q": "Scientology was literally invented in 1954 by a science fiction writer named L. Ron Hubbard. How does that make you feel about religion in general?",
        "options": [("😐 Every religion had a human founder", 0), ("🤔 At least older religions have more history", 1), ("😂 It shows how easily people accept invented mythology", 4), ("💀 Scientology just makes the origin of ALL religion more obvious", 5)]
    },
    {
        "q": "Scientology teaches that 75 million years ago an alien ruler named Xenu trapped souls on volcanoes. Is that more or less believable than other religious origin stories?",
        "options": [("❌ Far less believable — it's obviously fiction", 0), ("😬 Strange but all religions have unusual beliefs", 2), ("🤔 It's ridiculous — but so is a talking snake in a garden", 4), ("💀 Scientology just makes the absurdity of all religions visible", 5)]
    },
    {
        "q": "Scientology charges hundreds of thousands of dollars to reach its highest spiritual levels. Is that different from how mainstream churches and mosques operate financially?",
        "options": [("✅ Yes — mainstream religion isn't that transactional", 0), ("😐 Some churches do exploit people financially too", 2), ("😤 The monetisation of faith is universal — Scientology is just obvious about it", 4), ("💀 Every religion sells access to God — Scientology just has a price list", 5)]
    },
    {
        "q": "Mormonism was founded in 1830 by Joseph Smith who claimed an angel gave him golden plates. No one else saw them. How credible is that?",
        "options": [("🙏 God works through chosen individuals", 0), ("😐 It's no stranger than other revelation claims", 1), ("🤔 A private revelation with no witnesses is a red flag", 4), ("💀 Every religion started with one person's unverifiable claim", 5)]
    },
    {
        "q": "Hinduism has 33 million gods. Islam and Christianity say there is only one. All three can't be right. What does that mean?",
        "options": [("✅ Mine is right — the others are misled", 0), ("🤷 All religions point to the same ultimate truth", 2), ("😐 The contradiction itself is evidence against all of them", 4), ("💀 When everyone claims the one true God — nobody has the one true God", 5)]
    },
    {
        "q": "Ancient Egyptians, Greeks, and Romans all had gods that people once believed in completely. Those are now called myths. How is today's religion different?",
        "options": [("✅ Those were false gods — mine is real", 0), ("😐 History will judge — I believe what I believe", 2), ("🤔 Future generations may call today's religions myths too", 4), ("💀 There's no difference — today's religion is tomorrow's mythology", 5)]
    },

    # ── SOCIETY & AFRICA ──────────────────────────────────────────────────────
    {
        "q": "Africa is the most religious continent yet one of the poorest. Why?",
        "options": [("🙏 God tests those he loves most", 0), ("📖 Corruption not religion is the problem", 1), ("🤔 Religion keeps people passive and hoping", 4), ("💀 Religion replaced resistance with prayer", 5)]
    },
    {
        "q": "A pastor drives a Rolls Royce paid by his congregation. Your reaction?",
        "options": [("✅ God blesses his servants", 0), ("😬 Uncomfortable but maybe he earned it", 1), ("😤 That's exploitation plain and simple", 4), ("🤡 Religion was always a business", 5)]
    },
    {
        "q": "Religion says women should be submissive to men. Your reaction?",
        "options": [("✅ That's God's natural order", 0), ("😐 It's cultural not truly religious", 2), ("😤 That's not from God — that's from men", 4), ("💀 Religion was designed by men to control women", 5)]
    },
    {
        "q": "The Crusades, Jihad, Inquisition — religion and violence. Your verdict?",
        "options": [("🙏 Men twisted religion — God is not to blame", 0), ("😬 Religion was misused but it's not its nature", 1), ("📖 The holy books themselves fuel the violence", 4), ("💀 Religion is the most dangerous idea humans invented", 5)]
    },
    {
        "q": "Children raised in a religion they didn't choose — your take?",
        "options": [("✅ Good — they need a moral foundation", 0), ("🤷 Fine if they can question it later", 2), ("😕 Unfair to decide their beliefs for them", 4), ("🚨 Teaching kids they're born sinful is psychological harm", 5)]
    },

    # ── PHILOSOPHY ────────────────────────────────────────────────────────────
    {
        "q": "If God is all-powerful, can he create a rock so heavy he can't lift it?",
        "options": [("🙏 God is beyond such logical puzzles", 0), ("😐 It's a paradox not a real argument", 1), ("🤔 It shows the concept of all-powerful has internal contradictions", 4), ("💀 Omnipotence is a logically incoherent concept", 5)]
    },
    {
        "q": "The Euthyphro dilemma: Is something good because God commands it? Or does God command it because it's good?",
        "options": [("🙏 God defines goodness — the question is moot", 0), ("😐 God and goodness are one — no dilemma", 1), ("🤔 Either answer removes the need for God as a moral foundation", 4), ("💀 This dilemma alone destroys the divine command theory of ethics", 5)]
    },
    {
        "q": "If God stopped all evil tomorrow — would humans still have free will?",
        "options": [("✅ Free will requires the option to do evil", 0), ("🤷 It's a tough question I haven't resolved", 2), ("😐 That excuse doesn't cover natural disasters", 4), ("💀 Free will is just God's alibi for doing nothing", 5)]
    },
    {
        "q": "Religious people report higher happiness and live longer. Does that make religion true?",
        "options": [("✅ Yes — God blesses believers", 0), ("🤷 Maybe there's something real behind faith", 2), ("🧠 Community and routine cause that not God", 4), ("❌ Comfort doesn't make a lie true", 5)]
    },
    {
        "q": "Both Islam and Christianity say only their followers go to heaven. Both can't be right. So?",
        "options": [("✝️ Mine is right — the others are misled", 0), ("🤷 God judges the heart not the religion", 2), ("😐 That contradiction has always troubled me", 3), ("💀 It means both are probably wrong", 5)]
    },
    {
        "q": "You were born into your religion based on where you were born. If you'd been born in Saudi Arabia instead of the country you're now — would you be Muslim right now?",
        "options": [("🙏 God would have found me regardless", 0), ("😐 Probably — but I've made the faith my own", 2), ("🤔 That shows religion is mostly geography not truth", 4), ("💀 Your religion is an accident of birth not divine revelation", 5)]
    },
    {
        "q": "The problem of divine hiddenness — if God wants everyone to believe, why does he hide from billions?",
        "options": [("🙏 Faith requires seeking — God rewards those who seek", 0), ("😐 God reveals himself differently to different people", 2), ("🤔 A God who wants belief but hides makes no logical sense", 4), ("💀 A real God who wanted belief would simply show up", 5)]
    },
    {
        "q": "Who created God? If everything needs a cause, what caused God?",
        "options": [("🙏 God is uncaused — he exists outside time", 0), ("😐 Some things can exist without a cause", 2), ("🤔 Then why can't the universe just exist without a cause too?", 4), ("💀 The cosmological argument defeats itself", 5)]
    },

    # ── BONUS PROVOCATIVE ──────────────────────────────────────────────────────
    {
        "q": "Has God ever clearly answered your prayer in a way you can't explain?",
        "options": [("✅ Yes — many times without doubt", 0), ("🤷 Maybe — hard to say if it was coincidence", 2), ("😐 Not really — things just happened anyway", 4), ("❌ No — and I've stopped expecting it", 5)]
    },
    {
        "q": "How do you see organised religion?",
        "options": [("🏛️ Foundation of society and morality", 0), ("⚖️ Flawed but does some good", 2), ("⚔️ More harm than good historically", 4), ("🎪 Built to control, divide, and collect money", 5)]
    },
    {
        "q": "Where did the universe come from?",
        "options": [("✝️ God created it — full stop", 0), ("🌀 God may have triggered it somehow", 2), ("🔭 Science is still working it out", 3), ("⚡ Natural processes — no God required", 5)]
    },
    {
        "q": "How did humans come to exist?",
        "options": [("✝️ God created us as scripture says", 0), ("🌱 God guided evolution", 2), ("🔬 Evolution but something started it", 3), ("⚡ Pure evolution — no God needed", 5)]
    },
    {
        "q": "Teaching a child they were born sinful — is that harmful?",
        "options": [("✅ No — it teaches humility and need for God", 0), ("😐 Depends how it's framed", 2), ("😕 Telling a child they're broken from birth is damaging", 4), ("🚨 It's the original form of psychological manipulation", 5)]
    },
    {
        "q": "Satan and hellfire — are these real threats?",
        "options": [("😰 Yes — the devil is real and active", 0), ("😐 Satan is more of a symbol of evil", 2), ("🤔 These stop being my problem the moment I leave the religion", 4), ("😂 Religion invented Satan to make sure you never feel safe without it", 5)]
    },
    {
        "q": "The Quran says men can have up to 4 wives. The Bible says Solomon had 700. Is that from a God of love?",
        "options": [("✅ Different context — God allowed it then", 0), ("😐 It was cultural not a divine ideal", 1), ("😤 A God of love wouldn't build inequality into marriage", 4), ("💀 Both books were written by men who wanted more wives", 5)]
    },
    {
        "q": "If tomorrow scientists confirmed 100% that God does not exist — how would your life change?",
        "options": [("😰 Everything would collapse — God is my foundation", 0), ("😐 I'd be devastated but I'd adapt", 2), ("🤷 Not much honestly — I already live by my own values", 4), ("😌 Relief — I've been living without God anyway", 5)]
    },
    {
        "q": "Adam and Eve — a white couple apparently — couldn't biologically produce all of humanity's racial diversity. Does that matter?",
        "options": [("🙏 God could do anything — it's a miracle", 0), ("😐 The story is allegorical not biological", 2), ("🧬 Genetics makes the Adam and Eve story impossible literally", 4), ("💀 Humans predate Adam and Eve by 200,000 years", 5)]
    },
    {
        "q": "Most people fear death. Does religion offer a real solution to that fear or just a comfortable story?",
        "options": [("✅ Heaven is real — religion offers the truth", 0), ("😐 The comfort itself has value even if uncertain", 2), ("🤔 Comfortable stories are still just stories", 4), ("💀 Religion monetises death anxiety — that's its entire business model", 5)]
    },
]

def get_random_questions(n=10):
    return random.sample(ALL_QUESTIONS, min(n, len(ALL_QUESTIONS)))