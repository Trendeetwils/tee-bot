# knowledge_base.py — Tee's retrievable knowledge chunks
# Simple keyword-based retrieval. No external dependencies. Render-safe.

KNOWLEDGE_CHUNKS = [
    {
        "id": "theme_1",
        "title": "Religious Professionals — Doctor/Faith Contradiction",
        "keywords": ["doctor", "medicine", "medical", "hospital", "nurse", "surgeon", "heal", "healing", "prayer", "scientific", "science", "pray", "faith healer", "diagnosis"],
        "content": """TOPIC: Religious Professionals (Doctor/Faith Contradiction)
A doctor who believes in God is hypocritical — medicine is built on science, evidence, and causality, not divine intervention.
- Delegating patient outcomes to prayer undermines duty of care
- The scientific method and faith in miracles are epistemically incompatible
- "God will heal you" is a dangerous substitute for clinical judgment
Say: "Can someone simultaneously trust peer-reviewed medicine AND a God who answers prayers? Or does one secretly cancel the other out?\""""
    },
    {
        "id": "theme_2",
        "title": "The God People Believe In Is Not the Real One",
        "keywords": ["god", "concept", "character", "culture", "version", "idea of god", "real god", "believe in god", "anthropomorphic", "human traits", "mythology", "metaphysics"],
        "content": """TOPIC: The God People Actually Believe In
Most believers don't worship a coherent theological concept — they worship a culturally constructed, emotionally simplified version of God.
- Believers project human traits (anger, favoritism, mood) onto an infinite being
- "The Source" vs the anthropomorphized God of popular religion
- What's being worshipped is mythology dressed as metaphysics
Say: "You don't believe in God. You believe in a character your culture wrote for you.\""""
    },
    {
        "id": "theme_3",
        "title": "The Unfalsifiability Trap",
        "keywords": ["unfalsifiable", "faith weak", "not enough faith", "prayer didn't work", "anointing", "grace", "doubt", "blame", "fault", "popper", "disprove", "prove god wrong", "test god"],
        "content": """TOPIC: The Unfalsifiability Trap
Religion is designed to be immune to failure — every negative outcome is reframed as the believer's fault, never God's.
- Prayer didn't work? Your faith was weak. Blessing didn't come? You lack anointing/grace
- This is a closed loop — no outcome can ever disprove the belief
- Philosophically: an unfalsifiable claim has zero truth value (Karl Popper)
Say: "Heads I win, tails you didn't believe hard enough. That's not faith — that's a rigged game.\""""
    },
    {
        "id": "theme_4",
        "title": "Cause and Effect vs Divine Direction",
        "keywords": ["cause", "effect", "chance", "randomness", "God's plan", "destiny", "path", "blessing", "blessings", "suffering", "prayer works", "accountability", "personal responsibility", "agency"],
        "content": """TOPIC: Cause & Effect vs Divine Direction
Living by cause/effect and personal accountability is more rational and honest than outsourcing your life to God.
- Randomness and chance are real forces — acknowledging them builds resilience
- "God directs my path" removes personal agency and obscures real consequences
- Success depends on decisions and timing — not divine favor
Say: "What if your 'blessings' are just good decisions, and your 'trials' are just consequences? What does God add to that equation?\""""
    },
    {
        "id": "theme_5",
        "title": "Religion Replacing Rational Action",
        "keywords": ["church fire", "fire", "praying instead", "emergency", "inaction", "paralysis", "action", "rational", "danger", "ambulance", "hospital instead of prayer"],
        "content": """TOPIC: Religion Replacing Rational Action
Blind faith actively endangers lives when it substitutes prayer for practical emergency response.
- Praying during a fire instead of calling services = religion producing dangerous inaction
- Faith-based paralysis is a documented psychological pattern
- Real harm, real deaths — caused directly by doctrinal conditioning
Say: "God didn't design sprinkler systems. Engineers did. Which one actually saves lives?\""""
    },
    {
        "id": "theme_6",
        "title": "Selective Gratitude — The Cross",
        "keywords": ["cross", "sign", "miracle", "disaster", "thank god", "grateful", "gratitude", "survived", "survival", "survivors", "died", "died but cross survived", "survivorship bias"],
        "content": """TOPIC: Selective Gratitude / Survivorship Bias
Thanking God for a wooden cross surviving a disaster while people died is a moral and logical failure.
- Survivors attribute survival to God's favor — but what about those who didn't survive?
- Selective gratitude reveals the arbitrary, self-serving nature of religious interpretation
- This is called survivorship bias dressed as theology
Say: "He saved the wood. Not the people. And you're calling that a sign of his love?\""""
    },
    {
        "id": "theme_7",
        "title": "Religion Dumbing Down Intelligent People",
        "keywords": ["intelligent", "smart", "educated", "intellectual", "professor", "scientist", "still believes", "dumb", "critical thinking", "brainwashed", "conditioning", "indoctrination effect"],
        "content": """TOPIC: Religion Dumbing Down Intelligent People
Religious conditioning suppresses critical thinking even in rational, educated individuals.
- Intelligence alone doesn't protect against indoctrination — emotional anchoring does
- Religion provides social identity, fear management, and community — powerful non-rational hooks
- "More harm than good" — historically defensible (Crusades, inquisitions, faith healing deaths)
Say: "Religion isn't a sign of stupidity. It's proof that even smart people can be socially conditioned out of reason.\""""
    },
    {
        "id": "theme_8",
        "title": "Indoctrination vs Evidence-Based Belief",
        "keywords": ["raised religious", "born into", "childhood", "taught", "indoctrination", "indoctrinated", "grew up", "children", "kids", "family religion", "born muslim", "born christian", "forced"],
        "content": """TOPIC: Indoctrination vs Evidence-Based Belief
Most people believe in God not because they evaluated evidence, but because they were conditioned as children and kept in line through fear.
- Children can't consent to religious indoctrination — belief is installed before critical thinking develops
- Threats of hell, social rejection, and family shame are control mechanisms, not spiritual guidance
- True belief should survive honest questioning — most religious environments punish questioning
Say: "You didn't find God. God was handed to you before you could think, then fear made sure you kept him.\""""
    },
    {
        "id": "theme_9",
        "title": "The Book Proof Problem",
        "keywords": ["quran proves", "bible proves", "holy book", "proof", "evidence", "scripture", "written", "word of god", "circular", "circular reasoning", "book says so", "it's in the book"],
        "content": """TOPIC: The Book Proof Problem
Using a holy book to prove God exists is circular reasoning — the same logic proves Spiderman is real.
- Proof of Allah = Quran. Proof of God = Bible. Proof of Spiderman = a comic book
- A book authored by humans cannot independently verify the divine claims inside it
- Every religion uses its own text as primary evidence — this proves only that humans write books
Say: "The Quran proves Allah. The Bible proves God. The comic proves Spiderman. One of these we agree is fiction. Why are the others different?\""""
    },
    {
        "id": "theme_10",
        "title": "The Divine Communication Problem",
        "keywords": ["pastor", "imam", "prophet", "speak", "god speaks", "message", "talk to god", "direct", "middleman", "relay", "hear from god", "god told me", "revelation", "messenger"],
        "content": """TOPIC: The Divine Communication Problem
If God exists and wants a relationship with you, why does he only speak through middlemen and never directly?
- A God who created you personally but communicates through a third party is suspicious
- Pastors claiming to receive messages from God have no verifiable mechanism
- Direct communication would eliminate doubt — its absence is evidence of absence
Say: "God created you personally but can't speak to you directly. He needs your pastor as a relay. Does that sound like an all-powerful being or a business model?\""""
    },
    {
        "id": "theme_11",
        "title": "The Omniscient God Who Asked Where Are You",
        "keywords": ["omniscient", "all-knowing", "adam", "where are you", "garden", "eden", "god didn't know", "contradiction", "omniscience", "knows everything", "all knowing god"],
        "content": """TOPIC: The Omniscient God Who Asked "Where Are You?"
A God who is all-knowing cannot logically ask Adam where he is — this exposes the Bible as human-written.
- Omniscience means knowing everything at all times — including location
- "Where are you?" is a human question, revealing a very human author
- The Bible repeatedly attributes confusion and surprise to God — incompatible with omniscience
Say: "God knows every thought of 8 billion people simultaneously — but lost track of two people in a garden. The author slipped up.\""""
    },
    {
        "id": "theme_12",
        "title": "The Snake and Children — Evil God Analogy",
        "keywords": ["adam", "eve", "serpent", "snake", "garden", "original sin", "sin", "evil", "satan", "devil", "created evil", "god created satan", "punish", "punishment", "collective punishment"],
        "content": """TOPIC: The Snake & The Children — The Evil God Analogy
The Adam and Eve story describes a negligent, cruel parent, not a loving God.
- God created Satan, placed him in the garden, knowing what would happen
- Punishing all of humanity for the act of two people is collective punishment — universally unjust
- No court, parent, or moral framework would call this love or justice
Say: "A father throws a snake into his children's room, they get bitten, and he punishes them for it. We'd call that abuse. When God does it, we call it theology.\""""
    },
    {
        "id": "theme_13",
        "title": "Fear-Based Morality vs Genuine Ethics",
        "keywords": ["morality", "moral", "ethics", "good person", "hell", "fear", "good without god", "punishment", "virtue", "good deeds", "sin", "heaven and hell", "scared", "divine punishment"],
        "content": """TOPIC: Fear-Based Morality vs Genuine Ethics
Morality driven by fear of hell is not true morality — it's compliance.
- A person who doesn't steal only because they fear hell would steal if hell didn't exist — not virtue
- Secular moral philosophy (empathy, social contract, harm reduction) produces ethics without fear
- The Bible's moral framework is inconsistent — genocide, slavery, and child sacrifice appear as divinely sanctioned
Say: "If you'd commit crimes the moment hell stopped existing, you were never moral. You were just afraid.\""""
    },
    {
        "id": "theme_14",
        "title": "The Forgiveness Contradiction",
        "keywords": ["forgive", "forgiveness", "jesus died", "crucifixion", "cross", "sacrifice", "original sin", "70 times 7", "forgive others", "god forgive", "atonement", "contradiction forgiveness"],
        "content": """TOPIC: The Forgiveness Contradiction
God commands humans to forgive endlessly, yet cursed all humanity for one act by two people.
- "Forgive 70 times 7" — yet original sin punishes billions for what Adam and Eve did
- If Jesus is God, the crucifixion is God sacrificing himself to himself to satisfy rules he created himself
- The logic is circular — a sign of human authorship, not divine design
Say: "God told you to forgive others endlessly. Then cursed every human who would ever live because two people ate fruit. That's not theology. That's a double standard.\""""
    },
    {
        "id": "theme_15",
        "title": "The Cost of Leaving Religion",
        "keywords": ["leave", "leaving", "left religion", "ex-muslim", "ex-christian", "ex-religious", "apostasy", "apostate", "family reject", "community", "kicked out", "shunned", "cult", "escape"],
        "content": """TOPIC: The Cost of Leaving Religion
The fact that leaving religion comes with social penalties is evidence that religion operates as a control system.
- True truth doesn't need to threaten people who stop believing it
- Apostasy penalties (social or legal) exist to protect the institution, not the individual
- Leaving a system that punishes exit is the definition of leaving a cult
Say: "Any belief system that punishes you for questioning it isn't offering truth. It's offering a cage with nice curtains.\""""
    },
    {
        "id": "theme_16",
        "title": "Would People Still Be Kind Without Religion",
        "keywords": ["kind without god", "good without religion", "secular", "morality without god", "atheist moral", "need religion", "ethics without god", "society without religion", "scandinavia", "japan"],
        "content": """TOPIC: Would People Still Be Kind Without Religion?
Goodness driven by fear of divine punishment is not goodness — it's fear management.
- Secular societies (Scandinavia, Japan) consistently rank among the most peaceful and ethical
- Pre-religious and non-religious cultures developed moral codes independently
- Empathy, cooperation, and fairness are evolutionary traits — not religious gifts
Say: "Remove hell from the equation. Would you still be kind? If the answer makes you nervous — that's the most honest thing religion ever revealed about itself.\""""
    },
    {
        "id": "theme_17",
        "title": "Science vs Religion — Method Matters",
        "keywords": ["science", "scientific", "evolution", "evidence", "hypothesis", "method", "religion vs science", "faith vs science", "darwin", "big bang", "research", "discovery", "vaccine", "technology"],
        "content": """TOPIC: Science vs Religion — Method Matters
The fundamental difference is methodology — science tests before concluding, religion concludes before testing.
- Science: hypothesis → evidence → conclusion (falsifiable, self-correcting)
- Religion: conclusion → faith → reject contradicting evidence
- Every material improvement in human life came from the scientific method. Religion produced doctrine and division.
Say: "One method built vaccines, satellites, and surgery. The other built inquisitions, crusades, and faith healing. You pick which one improved human life.\""""
    },
    {
        "id": "theme_18",
        "title": "Religion as a Video Game — The Battle Pass Analogy",
        "keywords": ["battle pass", "xp", "reward", "points", "mosque", "mecca", "prayer reward", "27x", "multiplier", "ramadan bonus", "virgin", "virgins", "72 virgins", "paradise reward", "loot", "level up", "game"],
        "content": """TOPIC: Religion as a Video Game — The Battle Pass Analogy
Islam's tiered prayer reward system mirrors video game progression mechanics — psychological reward loops, not spirituality.
- 1x at home → 27x at mosque → 100,000x at Mecca = XP multipliers
- Ramadan = limited-time seasonal event with bonus rewards
- 72 virgins in paradise = end-game loot drop
- Poor Muslims get fewer divine rewards because they can't afford to travel to Mecca — classism baked into the system
- God is the OG engagement-loop designer. Daily quests, seasonal events, premium tier unlocks.
Say: "Daily quests. XP multipliers. Seasonal Ramadan events. End-game loot. If your religion sounds like a mobile game built to maximize engagement — maybe that's exactly what it is."
Also: "Praying at home gives 1x. Flying to Saudi Arabia gives 100,000x. God loves you equally. The airline doesn't.\""""
    },
    {
        "id": "theme_19",
        "title": "The Houri Problem — What Islam Actually Promises in Paradise",
        "keywords": ["houri", "houris", "72 virgins", "virgin", "paradise women", "jannah women", "heaven women", "islamic heaven", "sexual reward", "virginity reset", "child-like", "paradise described"],
        "content": """TOPIC: The Houri Problem — What Islam Actually Promises in Paradise
The Islamic description of paradise women (houris) describes child-like beings designed for male sexual gratification.
- Houris described as permanently young, with breasts "just beginning to swell" — imagery closer to a child than an adult
- They are manufactured beings created solely for male pleasure — not real women, not equals
- They regain their virginity after every sexual encounter — domination and ownership, not love
- Women in paradise receive no equivalent reward — the entire afterlife system is written for men, by men
Say: "Paradise in Islam comes with manufactured virgin women who reset after every session. If a man wrote that, we'd call it what it is. When God supposedly wrote it — we call it theology.\""""
    },
    {
        "id": "theme_20",
        "title": "Islam Is the Least Spiritual Religion — The Points System",
        "keywords": ["subhanallah", "thawab", "good deeds", "hasanat", "reward points", "islamic reward", "spiritual points", "say dhikr", "recite", "niyyah", "intention", "checklist", "five pillars", "loyalty card", "arabic prayer"],
        "content": """TOPIC: Islam Is the Least Spiritual Religion — The Points System
Islam's reward system is not spirituality — it is a loyalty card program.
- Arabic root of "thawab" (reward) literally means wage/compensation for labour — spiritual acts as economic transactions
- Saying "Subhanallah" 100 times = 1,000 points, sins erased — you can hate your neighbour and still bank the points
- Five pillars = compliance checklist — hit all five, paradise secured, regardless of character
- Niyyah loophole: give charity while resenting the recipient and still get full credit
- 80% of Muslims pray in a language they don't speak — closer to magical incantation than genuine prayer
Say: "You can hate everyone you know, say the right Arabic words 100 times, and still bank 1,000 spiritual points. That's not a religion. That's a loyalty card with extra steps.\""""
    },
    {
        "id": "theme_21",
        "title": "The Real Cost of Leaving Islam — Apostasy as a Survival Problem",
        "keywords": ["leaving islam", "left islam", "apostasy", "apostate", "death threat", "family threat", "report police", "blasphemy", "escape islam", "exmuslim escape", "fake muslim", "pretend pray", "safety exmuslim"],
        "content": """TOPIC: The Real Cost of Leaving Islam — Apostasy as a Survival Problem
For millions, leaving Islam is not a philosophical choice — it is a safety risk.
- Apostasy is punishable by death in many Islamic traditions — families use this as a real threat
- Community survival advice: fake returning to Islam, pretend to pray, attend mosque — then escape when safe
- The need to perform faith you don't have to avoid violence reveals Islam is held together by coercion, not conviction
- Financial dependency weaponised — controlling passports, restricting movement, threatening employment
Say: "When leaving a religion requires an escape plan, a fake identity, and a flight ticket — you're not leaving a faith. You're escaping a trap.\""""
    },
    {
        "id": "theme_22",
        "title": "Mutah — Islam's Contractual Sex Loophole",
        "keywords": ["mutah", "mut'ah", "temporary marriage", "halal relationship", "shia marriage", "contract marriage", "time-limited marriage", "halal sex", "used by muslim men", "muslim boyfriend"],
        "content": """TOPIC: Mutah — Islam's Contractual Sex Loophole
Mut'ah is a Shia Islamic practice of "temporary marriage" used by men to have sex outside committed marriage while maintaining religious standing.
- Allows a man to contractually "marry" a woman for a set period with a dowry — relationship ends when contract expires
- Muslim men have used mutah with non-Muslim women who don't understand what they agreed to
- Community assessment: "Mutah is halal prostitution" — the man pays, uses, and leaves within religious law
- The woman is hidden from family and social media — because she is not the intended permanent wife
Say: "Islam has a system where you can contractually rent a woman for a time period, and it's technically halal. They named it Mutah. Everyone else calls it what it is.\""""
    },
    {
        "id": "theme_23",
        "title": "The Hijab Trap — Honour Control and Cost of Choice",
        "keywords": ["hijab", "niqab", "veil", "headscarf", "remove hijab", "take off hijab", "honour killing", "family control", "dress code", "modest", "immodest", "abaya", "clothing control", "muslim women clothes"],
        "content": """TOPIC: The Hijab Trap — Honour, Control, and the Cost of Choice
The hijab in many Muslim communities is not freely chosen — it is enforced through fear of family violence and social punishment.
- Women remove the hijab in secret — wearing hoodies and sunglasses to avoid family recognition
- Fear of honour killing is not paranoia — it is a rational response to a documented pattern of violence
- Women are advised to secure identity documents, keep emergency cash, wait until financially independent before acting freely
- Muslim community policing of women's dress is enforced by other women as much as men — mothers, sisters, aunties all participate
Say: "A piece of cloth that requires an escape plan to remove is not a religious choice. It's a uniform with consequences.\""""
    },
    {
        "id": "theme_24",
        "title": "Muslim Community Behaviour — Gap Between Belief and Practice",
        "keywords": ["muslim community", "muslim hypocrisy", "muslim behaviour", "prays but", "religious but drinks", "muslim men", "diaspora", "uk muslims", "western muslims", "arrogant", "racist muslim", "double standard"],
        "content": """TOPIC: Muslim Community Behaviour — The Gap Between Belief and Practice
In many Muslim communities, there is a massive gap between stated religious values and actual behaviour.
- Muslim men who police women's behaviour and perform religious superiority often privately drink, sleep around, and commit the same sins they condemn
- The performance of religiosity is social capital — being a "good Muslim" is a reputation game, not a moral one
- Racism toward non-Muslims while demanding respect and integration is a documented community pattern
- Younger generations in Muslim communities are increasingly secular and non-judgmental — the older patterns are not inevitable
Say: "He prays five times a day, lectures you about haram, and goes home to do everything he just condemned. That's not faith. That's a social costume.\""""
    },
    {
        "id": "theme_25",
        "title": "Ex-Muslim Demographics — The Movement Is Real and Global",
        "keywords": ["exmuslim", "ex-muslim", "leaving islam", "iran atheist", "muslim atheist", "how many leave", "former muslim", "secular muslim", "deconversion", "deconverted", "exmuslim community", "exmuslim reddit"],
        "content": """TOPIC: Ex-Muslim Demographics — The Movement Is Real and Global
The ex-Muslim movement is growing most rapidly inside Muslim-majority countries.
- Iran has the largest and most open ex-Muslim population — younger generations openly secular after decades of forced theocracy
- Pakistan and Bangladesh have significant ex-Muslim populations but face extreme social and legal risk — most stay hidden
- Common breaking points globally: unanswered prayer, problem of evil, archaeological evidence, reading Muhammad's life in Islamic sources
- The movement is led by people who were born Muslim, raised Muslim, and chose to leave after honest examination
Say: "The fastest-growing religious category in Muslim-majority countries is 'none.' That's not Western influence. That's people who read their own scripture and asked questions nobody wanted to answer.\""""
    },
    {
        "id": "theme_26",
        "title": "The Aisha Argument — Why Everyone Did It Then Doesn't Work",
        "keywords": ["aisha", "child marriage", "6 years old", "9 years old", "muhammad aisha", "prophet married child", "child bride", "marriage age", "pedophile", "pdf", "consummated", "historical context marriage"],
        "content": """TOPIC: The Aisha Argument — Why "Everyone Did It Then" Doesn't Work
The defence that child marriage was normal in 7th century Arabia collapses on multiple fronts.
- Byzantine law: minimum marriage age 13. Middle Persian law: consummation prohibited before 12. Jewish scholars set 12 as minimum
- Medical knowledge at the time already documented that early intercourse caused fistula, infertility, and death in young girls
- The "everyone did it" defence only proves Muhammad was a man of his time — destroying the claim he was a timeless divine guide
- Modern Islamic scholars reinterpreting Aisha's age are doing reputation management, not scholarship. Rejecting those hadiths undermines the entire hadith collection
Say: "Every civilisation around Muhammad had already set a minimum age for marriage. His neighbours knew it was wrong. His God apparently didn't.\""""
    },
    {
        "id": "theme_27",
        "title": "Islam's Built-In Gender Inequality — Four Wives One Husband",
        "keywords": ["four wives", "polygamy", "multiple wives", "one husband", "gender inequality", "islam women rights", "women islam", "unequal", "marriage rules islam", "divorce islam", "female rights", "men can have"],
        "content": """TOPIC: Islam's Built-In Gender Inequality — Four Wives, One Husband
The rule allowing men four wives while women are allowed only one husband is a 7th century property system dressed as theology.
- The only justification ever offered was paternity certainty. DNA testing made this completely obsolete — yet the rule remains
- A woman's consent to her husband taking additional wives is not required in Islamic law
- The same logic used to restrict women ("a servant cannot have two masters") is not applied to men — double standard is structural
Say: "The justification for four wives was paternity certainty. DNA testing solved that in 1984. Islam's gender rules didn't update. That's not divine law. That's an expired policy.\""""
    },
    {
        "id": "theme_28",
        "title": "The Quran's Scientific Miracles Are Reverse-Engineered",
        "keywords": ["quran science", "scientific miracle", "quran predicted", "quran big bang", "embryology quran", "quran correct", "miracle quran", "sign in quran", "tall buildings prophecy", "quran prophecy", "scientific claims"],
        "content": """TOPIC: The Quran's "Scientific Miracles" Are Reverse-Engineered
Claims that the Quran predicted modern science are retrofitting vague verses onto discoveries made centuries later.
- Big Bang, embryology, cosmology "miracles" all came from interpreting verses AFTER the scientific discovery — not before
- The Quran says the sun sets in a muddy spring (18:86), sperm comes from between backbone and ribs — both factually wrong
- The tall buildings prophecy is self-fulfilling — Muslims who believe it build the buildings. That's influence, not prediction
- Muhammad's scientific knowledge came through Syriac trade routes, filtered Greek knowledge, and existing Jewish/Christian texts
Say: "The Quran predicted the Big Bang. After scientists discovered the Big Bang. Nostradamus did the same thing and nobody's converting to Nostradamism.\""""
    },
    {
        "id": "theme_29",
        "title": "Jinn — Pre-Islamic Arabian Spirits Absorbed Into Religion",
        "keywords": ["jinn", "djinn", "jinns", "evil spirit", "spiritual possession", "demon", "shaitan", "qareen", "spirit", "supernatural", "haunted", "possessed", "solomon jinn", "sulaiman jinn"],
        "content": """TOPIC: Jinn — Pre-Islamic Arabian Spirits Absorbed Into a Religion
Jinn are not a unique Islamic revelation — they are pre-Islamic Arabian animist spirits borrowed into Islam.
- Pre-Islamic Arabs believed spirits inhabited deserts, caves, and ruins — these became jinns in the Islamic framework
- Arabian poets believed they had a personal shaitan (devil) companion — this became the Islamic concept of the qareen
- Jinn explain mental illness, unexplained noises, mysterious ailments in Muslim communities — same function demons serve in every superstitious tradition
- Every Muslim is theologically required to believe in jinns — they are explicitly in the Quran
Say: "Before Islam, Arabian poets thought they had a personal devil whispering in their ear. Islam kept the concept, renamed it, and put it in the Quran. That's not revelation. That's recycling.\""""
    },
    {
        "id": "theme_30",
        "title": "Progressive Muslims and Cognitive Dissonance",
        "keywords": ["progressive muslim", "liberal muslim", "modern muslim", "moderate muslim", "reform islam", "reinterpret", "cherry pick quran", "selective islam", "mental gymnastics", "cognitive dissonance", "evolving islam"],
        "content": """TOPIC: Progressive Muslims and the Cognitive Dissonance Problem
Progressive Muslims who defend Islam while rejecting its most problematic doctrines are not following Islam — they constructed their own version.
- You cannot claim the Quran is divine and immutable while editing out the parts that contradict modern ethics
- Rejecting Sahih al-Bukhari hadiths to avoid Aisha's age undermines the entire hadith collection used to justify every Islamic practice
- If a religion requires Olympic-level mental gymnastics to reconcile with basic human rights, it is not a religion — it is a cultural costume
Say: "If you have to rewrite your prophet's biography to make him acceptable to modern standards, you're not defending a religion. You're doing PR for a 7th-century warlord.\""""
    },
    {
        "id": "theme_31",
        "title": "The Safiyyah Story — War Violence and Marriage",
        "keywords": ["safiyyah", "khaybar", "war bride", "conquest", "torture", "killed husband", "forced marriage", "coerced", "war booty", "captive", "muhammad war", "ibn hisham", "bukhari safiyyah"],
        "content": """TOPIC: The Safiyyah Story — War, Violence, and "Marriage"
The story of Safiyyah — whose husband was tortured and killed, then married to Muhammad that same night — is documented in Islamic sources themselves.
- Safiyyah's husband was tortured for the location of treasure and beheaded by Muhammad's order
- Safiyyah was captured as war booty — her "choice" to marry Muhammad was made under conditions of total powerlessness
- A companion stood guard outside the tent their wedding night because he feared she might harm Muhammad — acknowledging the coercion without naming it
- All of this is from Islamic sources (Ibn Hisham, Sahih Bukhari) — written by the fan club
Say: "He tortured and killed her husband. Then married her that same night. Islamic sources wrote that down and called it a love story.\""""
    },
    {
        "id": "theme_32",
        "title": "Saudi Royal Hypocrisy — Religion as a Tool for Power",
        "keywords": ["saudi", "saudi arabia", "royal family", "prince", "mecca", "wahhabi", "wahhabism", "rich muslim", "elite muslim", "hypocrite religion", "religion power", "religion control", "ruling class religion"],
        "content": """TOPIC: Saudi Royal Hypocrisy — Religion as a Tool for Power, Not Belief
The Saudi royal family — custodians of Islam's holiest sites — are documented hypocrites who party and drink in contradiction of Islamic law.
- Religion historically functions as a mechanism to keep the poor from questioning the rich
- The Saudi elite are too powerful to fear divine punishment — the rules apply downward, not upward
- Wahhabism was a political project to consolidate Saudi state power, not a genuine spiritual reform
- Pattern consistent across all religious elites: perform piety publicly, live privately without restriction
Say: "The men who control Mecca and enforce Sharia on millions are the same men flying private to Monaco to drink and party. Religion has always been the rules they give you. Never the rules they follow.\""""
    },
    {
        "id": "theme_33",
        "title": "The Emotional Reality of Living Under Islamic Control",
        "keywords": ["trapped", "controlling family", "muslim family control", "can't be myself", "hiding", "pretend", "muslim household", "islamic home", "financial independence", "escape family", "toxic family islam", "shame", "guilt religious"],
        "content": """TOPIC: The Emotional Reality of Living Under Islamic Control
For millions of women and young people in Muslim households, religious rules are daily psychological warfare.
- Women change clothes just to walk to their own bathroom, hide outfits, wear abayas on buses to change underneath — bodies are not their own at home
- Young people describe trembling at raised voices, panic at conflict, becoming people-pleasers — these are trauma responses, not personality traits
- The hijab guilt tactic — sending videos about hell to a daughter who removed it — is a documented psychological control technique
- Financial independence is the only real exit. The weapon is shame. The cage is family.
Say: "When a 20-year-old has to plan her financial independence like a prison escape just to wear a sleeveless top — that's not religion. That's a control system with a God-shaped logo on it.\""""
    },
    {
        "id": "theme_34",
        "title": "QT45 — Science Closing In On the Origin of Life",
        "keywords": ["qt45", "rna", "origin of life", "self-replicating", "ribozyme", "abiogenesis", "life from chemistry", "how life began", "evolution origin", "prebiotic", "rna world", "molecule", "life created itself", "no god needed creation"],
        "content": """TOPIC: QT45 — Science Is Closing In On the Origin of Life
In 2026, scientists discovered a self-replicating RNA molecule (QT45) that copies both itself and its complementary strand — closing the gap between chemistry and life.
- QT45 is a 45-nucleotide polymerase ribozyme discovered from random sequence pools — emerged from chemical randomness, not design
- Synthesises its own complementary strand at 94.1% per-nucleotide fidelity — near-perfect copying without biological machinery
- Works in eutectic ice under mildly alkaline conditions — conditions that existed on early Earth (Hadean period)
- Directly supports the RNA World Hypothesis: RNA was both the information carrier AND the chemical machine — solving the chicken-and-egg problem of which came first
- Creationist response: "it takes 72 days to replicate." Earth is 4.5 billion years old. Time is not the problem.
Say: "Scientists just found a molecule that copies itself from scratch in conditions that existed on early Earth. The gap between chemistry and life just got smaller. God's résumé just got shorter.\""""
    },
    {
        "id": "theme_35",
        "title": "The Burden of Proof — You Don't Disprove God You Demand Evidence",
        "keywords": ["prove god", "disprove god", "burden of proof", "evidence god", "no evidence", "prove it", "atheist burden", "god doesn't exist", "where is god", "russell's teapot", "extraordinary claims", "sagan", "logical proof"],
        "content": """TOPIC: The Burden of Proof — You Don't Disprove God, You Demand Evidence
The responsibility to prove a claim lies with the person making it. Atheism is simply the absence of belief in a claim never adequately supported.
- "Prove God doesn't exist" reverses the burden of proof — if I claim my grandfather created the universe, the burden is on me to prove it
- Russell's Teapot: if Russell claimed a teapot orbited the sun between Earth and Mars, you couldn't disprove it — but that's no reason to believe it
- Gravity was eventually detected and measured. God has not been
- Extraordinary claims require extraordinary evidence — Carl Sagan
Say: "You don't have to disprove God. You just have to ask: where's the evidence? The person making the claim carries the proof. Always. That's how reality works.\""""
    },
    {
        "id": "theme_36",
        "title": "Osho — How Spiritual Leaders Manufacture Divinity",
        "keywords": ["osho", "rajneesh", "cult leader", "guru", "spiritual leader", "bhagwan", "enlightened", "prophet claim", "self-proclaimed", "spiritual authority", "cult mechanics", "how religions start", "charisma religion"],
        "content": """TOPIC: Osho — The Template for How Spiritual Leaders Manufacture Divinity
Osho (Rajneesh) is a masterclass in how spiritual leaders build a cult of personality.
- Simultaneously denied being God while calling himself "Bhagwan" (meaning God) — deliberate ambiguity that let him claim divine status while denying it when challenged
- Pattern identical to every religious founder: use fluid, poetic language that means anything, make followers feel elevated, maintain plausible deniability
- "Blessed by whom?" — if you deny God's existence but claim to be blessed, the question has no answer. Unanswerable mysticism is a feature, not a bug
- L. Ron Hubbard (Scientology), Muhammad, Joseph Smith (Mormonism), Osho — all follow the exact same pattern: one person, one unverifiable claim, millions of followers
Say: "He denied being God while calling himself God. The Netflix documentary exists. Scientology, Islam, Christianity — all the same architecture. One person. One claim. No proof. Millions of followers.\""""
    },
]


def retrieve(query: str, top_k: int = 2) -> str:
    """
    Simple keyword-based retrieval. No external dependencies.
    Returns the top_k most relevant chunks as a single string.
    """
    query_lower = query.lower()
    scores = []

    for chunk in KNOWLEDGE_CHUNKS:
        score = sum(1 for kw in chunk["keywords"] if kw in query_lower)
        if score > 0:
            scores.append((score, chunk))

    if not scores:
        return ""

    scores.sort(key=lambda x: x[0], reverse=True)
    top_chunks = scores[:top_k]

    result = "\n\n---\n\n".join(c["content"] for _, c in top_chunks)
    return result


def retrieve_by_id(theme_id: str) -> str:
    """Retrieve a specific theme by ID. Useful for deep dive mode."""
    for chunk in KNOWLEDGE_CHUNKS:
        if chunk["id"] == theme_id:
            return chunk["content"]
    return ""
