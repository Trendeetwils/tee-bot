import random

# ═══════════════════════════════════════════════════════════════════════════════
# QUESTION CATEGORIES — each test pulls at least 1 from each category
# ═══════════════════════════════════════════════════════════════════════════════
# Categories:
#   scripture      — Bible/Quran/Vedas text contradictions and errors
#   hell           — Hell, punishment, afterlife
#   suffering      — Poverty, pain, God's inaction
#   health         — Doctors, medicine, healing, miracles
#   accident       — Survival, death, God's will in life events
#   death          — Who controls death, God's plan, dying
#   success        — Prayer and success, hard work vs faith
#   myth           — Borrowed traditions, pagan origins
#   morality       — God's moral commands, violence, slavery
#   science        — Evolution, Big Bang, archaeology
#   hope           — Purpose, meaning, faith without evidence
# ═══════════════════════════════════════════════════════════════════════════════

CHRISTIANITY_QUESTIONS = {

    "scripture": [
        {"q": "The Bible has been translated over 450 times by human hands.\n\nWhich version is the actual word of God?", "options": [("✅ The core message stays the same", 0), ("😐 The original manuscripts matter most", 1), ("💀 If God wrote it — why did humans keep rewriting it?", 5)]},
        {"q": "Matthew and Luke give completely different genealogies for Jesus.\n\nThey can't both be right.", "options": [("🙏 One traces Joseph's line — one traces Mary's", 0), ("😐 Different purposes — not a contradiction", 1), ("💀 The first chapter of the New Testament already has an error", 5)]},
        {"q": "The Bible says rabbits chew their cud (Leviticus 11:6).\n\nThey don't. Does that concern you?", "options": [("✅ Translation issue — not a scientific claim", 0), ("😐 Ancient classification systems were different", 1), ("💀 God apparently didn't know what rabbits eat", 5)]},
        {"q": "The Bible says bats are birds (Leviticus 11:19).\n\nThey are mammals. Does God not know the difference?", "options": [("✅ Ancient taxonomic categories differ", 0), ("😐 The classification system was different", 1), ("💀 God made bats — yet apparently didn't know they were mammals", 5)]},
        {"q": "God is described as unchanging (Malachi 3:6) yet he changed his mind about destroying Nineveh (Jonah 3:10).\n\nWhich is it?", "options": [("🙏 Changing action isn't changing his nature", 0), ("😐 His character is unchanging — his responses vary", 1), ("💀 The Bible contradicts itself on a fundamental attribute of God", 5)]},
        {"q": "God regretted making humans (Genesis 6:6).\n\nCan an all-knowing God be surprised or regretful?", "options": [("🙏 It's expressing God's emotional response not a knowledge failure", 0), ("😐 Anthropomorphic language to help humans understand God", 1), ("💀 An all-knowing God cannot regret — the Bible contradicts itself", 5)]},
        {"q": "The Bible says the mustard seed is the smallest seed (Matthew 13:32).\n\nIt isn't — many seeds are smaller. Does that matter?", "options": [("✅ It was a common illustration not a botany lesson", 0), ("😐 Jesus was speaking to his audience's understanding", 1), ("💀 An omniscient God made a factual error about seeds", 5)]},
        {"q": "The resurrection is the foundation of Christianity. Yet the four gospels give contradictory accounts of who saw the empty tomb first.", "options": [("✅ Minor differences don't affect the core truth", 0), ("😐 Different witnesses notice different details", 1), ("💀 Contradictory testimonies would be dismissed in any court", 5)]},
        {"q": "Paul wrote most of the New Testament yet never met Jesus.\n\nHow much weight should his words carry?", "options": [("✅ He was called by the risen Christ directly", 0), ("😐 His revelation was genuine", 1), ("💀 Christianity was largely designed by a man who persecuted Christians first", 5)]},
        {"q": "The Dead Sea Scrolls show key messianic prophecies about Jesus were added or edited centuries after the events.\n\nDoes that concern you?", "options": [("🙏 God preserved the essential truth", 0), ("😐 Minor textual variants don't change the message", 1), ("💀 The prophecies were written to fit — not fulfilled naturally", 5)]},
        # ── KB additions ──
        {"q": "God is all-knowing yet asked Adam 'Where are you?' in the garden.\n\nWhat does that reveal?", "options": [
            ("Started a conversation — God wasn't lost 🌿", 1),
            ("Teaching moment — not a literal question", 3),
            ("An all-knowing God cannot be surprised 🧐", 5),
        ]},
        {"q": "What's your best evidence that God exists?", "options": [
            ("The Bible says so — it's God's word 📖", 1),
            ("Personal experience and the universe", 3),
            ("A book proving itself is circular reasoning 🔁", 5),
        ]},
        {"q": "God tells us to forgive endlessly yet cursed all humanity for what two people did.\n\nConsistent?", "options": [
            ("His ways are beyond our understanding 🕊️", 1),
            ("It's complex — there's probably a reason", 3),
            ("Forgive all, yet punish billions 🚩", 5),
        ]},
    ],

    "hell": [
        {"q": "Hell — eternal torture for rejecting God.\n\nA God who sentences people to eternal fire is what exactly?", "options": [("😰 Just — he warned us", 0), ("😐 Hell is separation from God not literal fire", 2), ("💀 Hell is a control mechanism — not justice", 5)]},
        {"q": "You lived 80 years and rejected God.\n\nYou burn forever.\n\nEternal punishment for a finite life — is that justice?", "options": [("😰 God is both loving and just", 0), ("😐 The choice was yours", 1), ("💀 That's not justice — that's sadism", 5)]},
        {"q": "Revelation describes a God who throws people into a lake of fire for eternity.\n\nIs that the same loving God of John 3:16?", "options": [("😰 God is both loving and just", 0), ("😐 Revelation is highly symbolic", 1), ("💀 A being who tortures people forever cannot be called loving", 5)]},
        {"q": "Christianity teaches non-believers go to hell. Over 4 billion people on Earth are non-Christian.\n\nIs a God who condemns them loving?", "options": [("😐 God gives everyone enough light to respond", 0), ("🤷 His mercy is broader than we know", 2), ("💀 The numbers alone make Christian exclusivism morally indefensible", 5)]},
        {"q": "If Christianity is the only path to God — what happens to the billions who lived before Jesus or never heard of him?", "options": [("🙏 God judges them by the light they had", 0), ("😐 God's mercy extends beyond what we understand", 2), ("💀 The math on Christian salvation has always been a problem", 5)]},
    ],

    "suffering": [
        {"q": "God watches children suffer from cancer, war, and famine. Yet he does nothing.\n\nWhy?", "options": [("🙏 He gives humans free will", 0), ("😐 His ways are higher than ours", 1), ("💀 A God who watches children suffer and does nothing is not good", 5)]},
        {"q": "Job lost his children, wealth, and health because God made a bet with Satan.\n\nHow do you feel about that?", "options": [("🙏 God restored everything — it shows his faithfulness", 0), ("😐 It demonstrates the depth of faith God desires", 1), ("💀 Job's dead children weren't restored — new ones don't replace them", 5)]},
        {"q": "In 2 Kings 6:28-29 a mother boils and eats her own son during a siege.\n\nGod is watching. He does nothing. What does that tell you?", "options": [("😐 It was a consequence of Israel's sin", 0), ("🤔 I find those passages very hard to accept", 2), ("💀 There is no theology that makes this acceptable", 5)]},
        {"q": "Some of the most devout believers in the world live in extreme poverty.\n\nIs God testing them — or has religion taught them to accept what they should be fighting?", "options": [("🙏 God tests those he loves most", 0), ("😐 Poverty is a human problem not God's fault", 2), ("💀 Teaching the poor to pray instead of organise is the oldest tool of control", 5)]},
        {"q": "Prosperity gospel pastors preach that faith brings wealth.\n\nTheir congregations are poor. The pastor drives a Rolls Royce.\n\nWhose faith is actually working?", "options": [("🙏 God blesses his servants", 0), ("😐 Not all pastors are like that", 2), ("💀 Religion has always been most profitable for the people selling it", 5)]},
        # ── KB additions ──
        {"q": "Leaving Christianity means losing family and community.\n\nWhat does that say about the faith?", "options": [
            ("Shows how sacred the commitment is 🛐", 1),
            ("Harsh, but faith itself can still be valid", 3),
            ("Any belief that punishes exit is a cage 🔓", 5),
        ]},
        {"q": "Studies show religious people report higher satisfaction.\n\nProof that faith works?", "options": [
            ("God gives peace the world can't give 😊", 1),
            ("Helps some people even if not literally true", 3),
            ("Secular nations score highest on wellbeing 📊", 5),
        ]},
        {"q": "Teaching kids they're born sinful and could face hell.\n\nIs that love or harm?", "options": [
            ("It prepares them spiritually — it's love ❤️‍🔥", 1),
            ("Good intention — delivery can hurt though", 3),
            ("Threatening a child with eternal fire is abuse 🧠", 5),
        ]},
    ],

    "health": [
        {"q": "You got sick. The doctor treated you. You recovered.\n\nWho do you thank first — God or the doctor?", "options": [("🙏 God — he guided the doctor's hands", 0), ("😐 Both deserve credit", 2), ("💀 If God gets the credit — what exactly does the doctor get?", 5)]},
        {"q": "Christians pray for healing yet hospitals exist.\n\nIf prayer worked — why do we need medicine?", "options": [("🙏 God works through doctors and medicine", 0), ("😐 Prayer and medicine complement each other", 1), ("💀 We built hospitals because prayer alone doesn't work", 5)]},
        {"q": "If God answers prayer — why do amputees never regrow limbs?\n\nCancers disappear, headaches clear — but limbs never regenerate.", "options": [("🙏 God heals according to his purpose not our requests", 0), ("😐 We don't understand why God heals some things and not others", 2), ("💀 God heals things that heal anyway and ignores things that don't", 5)]},
        {"q": "Studies with proper controls show prayer has the same statistical outcome as no prayer.\n\nHow do you explain answered prayers?", "options": [("🙏 God can't be tested by scientific methods", 0), ("😐 Faith isn't about statistical proof", 2), ("💀 Confirmation bias explains answered prayer better than God does", 5)]},
        {"q": "Two people get the same diagnosis. One prays constantly and dies. One never prays and survives.\n\nWhat does that tell you about prayer and healing?", "options": [("🙏 God's plan differs for each person", 0), ("😐 Prayer isn't a guarantee — it's communion with God", 2), ("💀 Survival correlates with treatment — not prayer", 5)]},
        # ── KB addition ──
        {"q": "Someone survives illness and credits God.\n\nYour honest take?", "options": [
            ("God heard their prayers and healed them 🙏", 1),
            ("Prayer helped their mindset at least", 3),
            ("Doctors saved them. Prayer took the credit 🏥", 5),
        ]},
    ],

    "accident": [
        {"q": "A plane crashes. 200 people die. 3 survive.\n\nThe 3 survivors say 'God saved me.'\n\nWhat did God say to the other 200?", "options": [("🙏 God's plan included all of them", 0), ("😐 We can't understand why God intervenes sometimes and not others", 1), ("💀 Survivors claiming divine protection is just survivor bias dressed as theology", 5)]},
        {"q": "You survived a car crash that killed the other driver.\n\nWas God protecting you?\n\nIf yes — what did the other driver do wrong?", "options": [("🙏 God protected me — his plan for the other person was different", 0), ("😐 I don't think God intervenes in every accident", 2), ("💀 Randomness explains accident survival better than divine selection", 5)]},
        {"q": "You survived something that should have killed you.\n\nMost people call it a miracle.\n\nBut if God chooses who survives — he also chooses who doesn't.\n\nIs that the God you believe in?", "options": [("🙏 Yes — God controls all outcomes", 0), ("😐 God doesn't control every outcome — but he was with me", 2), ("💀 Physics and biology explain survival better than divine selection", 5)]},
        {"q": "Someone prays during a natural disaster and survives.\n\nThousands of equally faithful people die in the same event.\n\nHow do you explain that?", "options": [("🙏 God's ways are higher than ours", 0), ("😐 Faith doesn't guarantee physical safety", 2), ("💀 Survival in disasters correlates with geography and structure — not faith", 5)]},
    ],

    "death": [
        {"q": "When a child dies from cancer — people say 'it was God's will.'\n\nWhen a doctor saves a child — people say 'God is good.'\n\nWhich one is actually God's will?", "options": [("🙏 Both — God works through doctors and allows death for his purposes", 0), ("😐 God's will is complex — both can be true", 2), ("💀 'God's will' is a phrase that protects faith from falsification", 5)]},
        {"q": "If God controls when you die — why do people go to hospital?\n\nIf it's your time — nothing can stop it.\n\nIf it's not — you don't need help.", "options": [("🙏 God works through medicine to extend life", 0), ("😐 We use the resources available — God decides the outcome", 2), ("💀 Seeking medicine is an implicit acknowledgement that prayer alone doesn't determine survival", 5)]},
        {"q": "Is death God's will — or just biology?\n\nBecause if God decides when everyone dies — he also decided every genocide, famine, and child killed in war.", "options": [("🙏 God permits death — he doesn't author evil", 0), ("😐 Death is a consequence of the fall — not God's direct will", 2), ("💀 If God controls death — he has a lot to answer for", 5)]},
        {"q": "Every believer eventually dies — just like every non-believer.\n\nFaith doesn't extend life statistically.\n\nDoes that challenge the idea that God rewards the faithful?", "options": [("🙏 Rewards come in the afterlife — not this one", 0), ("😐 Faith isn't about living longer — it's about living better", 2), ("💀 A reward system with no verifiable payoff is indistinguishable from no reward system", 5)]},
    ],

    "success": [
        {"q": "If someone works hard for years and succeeds without religion — what does that say about faith being necessary?", "options": [("🙏 Success is part of God's plan whether they realise it or not", 0), ("😐 Faith isn't required for worldly success", 2), ("💀 If success doesn't need God — what role does faith actually play?", 5)]},
        {"q": "Two people pray for success. One succeeds, one fails.\n\nHow do you explain that?", "options": [("🙏 God answers differently for everyone", 0), ("😐 Sometimes the answer is no", 1), ("💀 If outcomes don't change — what does prayer actually do?", 5)]},
        {"q": "Some of the most successful people in the world don't follow any religion.\n\nWhat does that suggest?", "options": [("🙏 God blesses who he wills", 0), ("😐 Success isn't tied to belief", 2), ("💀 Success clearly operates independently of faith", 5)]},
        {"q": "If prayer worked reliably — wouldn't the most religious societies be the most successful?\n\nThe data shows the opposite.", "options": [("🙏 Success isn't the goal of faith", 0), ("😐 Many factors influence success", 1), ("💀 If prayer worked — results would be obvious", 5)]},
        {"q": "You worked hard for 10 years and built something meaningful.\n\nYou thank God.\n\nBut you made the calls, you showed up, you did the work.\n\nAt what point does the credit belong to you?", "options": [("🙏 All good things come from God — my effort was his gift", 0), ("😐 I give God credit but I know I worked hard too", 2), ("💀 Taking your own success and giving it to God is a form of self-erasure", 5)]},
        {"q": "If a non-believer lives a good life and a believer lives a harmful one — who deserves a better outcome?", "options": [("🙏 Faith matters more than actions in God's accounting", 0), ("😐 Both faith and actions matter", 1), ("💀 Judging based on belief over actions doesn't seem just", 5)]},
    ],

    "myth": [
        {"q": "Christmas trees, Easter eggs, even the name Easter — all from pagan traditions.\n\nDoes that concern you?", "options": [("🙏 We gave them Christian meaning", 0), ("😐 Minor borrowing doesn't affect truth", 1), ("💀 Christianity was built on recycled mythology", 5)]},
        {"q": "The flood story in the Bible mirrors the Babylonian Epic of Gilgamesh — written 1000 years earlier almost word for word.\n\nCoincidence?", "options": [("🙏 The same flood — different cultures recorded it", 0), ("😐 Shared memory of a real event", 1), ("💀 Biblical stories are recycled mythology from older civilisations", 5)]},
        {"q": "Christianity borrowed the dying-and-rising god story from Osiris, Dionysus, and Mithras — all predating Jesus.\n\nDoes that matter?", "options": [("✅ Those were false prophecies pointing to the real thing", 0), ("😐 Superficial similarities don't disprove Christianity", 1), ("💀 Jesus is the latest version of a very old myth", 5)]},
        {"q": "The Ten Commandments mirror the 42 Laws of Ma'at from ancient Egypt — written 1000 years earlier.\n\nWas Moses inspired — or copying?", "options": [("🙏 God revealed the same truth in different cultures", 0), ("😐 Moral principles appear across cultures independently", 2), ("💀 The Commandments are rebranded Egyptian moral law", 5)]},
    ],

    "morality": [
        {"q": "The Bible approves of slavery (Ephesians 6:5, Exodus 21:20).\n\nHow do you explain that?", "options": [("✅ Different era — cultural context", 0), ("😐 God allowed it but didn't endorse it", 1), ("💀 This alone proves the Bible was written by slave owners", 5)]},
        {"q": "God commanded genocide of entire nations including infants (1 Samuel 15:3).\n\nIs that the act of a moral being?", "options": [("😐 The Canaanites were deeply corrupted — it was judgment", 0), ("🤔 I struggle with those passages genuinely", 2), ("💀 If a human ordered that today we'd call them a war criminal", 5)]},
        {"q": "God told Abraham to kill his own son Isaac.\n\nWhat does that tell you about God?", "options": [("🙏 It was a test of faith — he stopped it", 0), ("😐 It shows God demands ultimate trust", 1), ("💀 Any parent who hears voices telling them to kill their child needs help not worship", 5)]},
        {"q": "Deuteronomy 22:28-29 says a rape victim must marry her rapist.\n\nWhat does that tell you about the Bible?", "options": [("😐 Different cultural and legal context", 0), ("🤔 That verse has always disturbed me", 2), ("💀 This verse alone proves the Bible was written by men — not God", 5)]},
        {"q": "God hardened Pharaoh's heart (Exodus 9:12) then punished Egypt for Pharaoh's hard heart.\n\nIs that fair?", "options": [("🙏 God's purposes are beyond our understanding", 0), ("😐 It demonstrates God's power over all things", 1), ("💀 That's entrapment — not justice", 5)]},
        {"q": "God killed 70,000 Israelites because King David took a census (2 Samuel 24).\n\nThe people did nothing wrong. Is that just?", "options": [("🙏 God's justice operates differently than ours", 0), ("😐 Sin has consequences that ripple outward", 1), ("💀 That's collective punishment — a war crime by modern standards", 5)]},
        # ── KB additions ──
        {"q": "Why do you try to be a good person?", "options": [
            ("God is watching — I fear judgment 😇", 1),
            ("Faith and genuinely caring for people", 3),
            ("Empathy. Fear of hell isn't real morality ⚖️", 5),
        ]},
        {"q": "Your prayer didn't get answered.\n\nWhy?", "options": [
            ("My faith wasn't strong enough 🙏", 1),
            ("Maybe it wasn't God's timing", 3),
            ("Prayer doesn't change outcomes 🎯", 5),
        ]},
    ],

    "science": [
        {"q": "Science shows the universe is 13.8 billion years old.\n\nGenesis says 6 days.\n\nWho's right?", "options": [("✅ Genesis — God's word over science", 0), ("😐 The 6 days are symbolic not literal", 2), ("💀 The math alone makes young earth creationism impossible", 5)]},
        {"q": "How do you explain the existence of dinosaurs — which lived 65 million years ago — when Genesis says the world began a few thousand years ago?", "options": [("✅ The fossil record is misinterpreted", 0), ("😐 The days in Genesis represent long ages", 2), ("💀 Dinosaurs alone disprove young earth creationism completely", 5)]},
        {"q": "The Bible says the earth has foundations and pillars (Job 9:6).\n\nWe know it's a sphere floating in space.\n\nYour take?", "options": [("✅ Poetic language describing stability", 0), ("😐 Ancient cosmological imagery not literal geography", 1), ("💀 The authors of the Bible genuinely believed the earth had physical pillars", 5)]},
        {"q": "Matthew 27:52-53 says dead saints rose from graves and walked into Jerusalem after Jesus died.\n\nWhy does no historian mention this?", "options": [("🙏 God didn't require secular documentation", 0), ("😐 Historians of the time focused on political events", 1), ("💀 The most dramatic event imaginable left zero historical trace because it didn't happen", 5)]},
        # ── KB additions ──
        {"q": "When science and the Bible contradict — which do you trust?", "options": [
            ("Scripture — God's word over science 📜", 1),
            ("Depends on the topic, I try to balance both", 3),
            ("Science. It's self-correcting and evidence-based 🔬", 5),
        ]},
        {"q": "A brilliant scientist believes in God.\n\nWhat does that prove?", "options": [
            ("Even the smartest recognise God is real 🧬", 1),
            ("Smart people hold different beliefs", 3),
            ("Smart people get conditioned too 🎓", 5),
        ]},
    ],

    "hope": [
        {"q": "If someone finds purpose and happiness without religion — does that challenge the idea that faith is necessary?", "options": [("🙏 True purpose ultimately comes from God", 0), ("😐 People can find meaning in different ways", 2), ("💀 If meaning exists without faith — what makes faith necessary?", 5)]},
        {"q": "Hope is real. Prayer feels real. Community feels real.\n\nBut are those things evidence of God — or evidence that humans need structure and meaning?\n\nYou can have all of those without a deity.", "options": [("🙏 Those feelings are God's presence", 0), ("😐 Both explanations could be true", 2), ("💀 Religion is extraordinarily good at meeting human psychological needs — that's not proof it's true", 5)]},
        {"q": "Christianity split into over 45,000 denominations all reading the same Bible.\n\nWhat does that tell you?", "options": [("😐 Humans interpret differently — the core truth remains", 0), ("🤔 That many splits suggests the text is genuinely ambiguous", 2), ("💀 If God wrote it clearly — why can't anyone agree on what it says?", 5)]},
        # ── KB additions ──
        {"q": "Without God, what's the point of life?", "options": [
            ("There isn't one — only God gives meaning 🌟", 1),
            ("Hard, but people find their own purpose", 3),
            ("Meaning is made, not handed down 🔥", 5),
        ]},
        {"q": "You feel God's presence during prayer.\n\nWhat does that actually mean?", "options": [
            ("God is communicating with me directly 🙌", 1),
            ("It feels real — I'm unsure what it is", 3),
            ("Same as every religion — just my brain 🧩", 5),
        ]},
        {"q": "'Prove God doesn't exist.' Your reaction?", "options": [
            ("Fair point — you can't disprove him 🤷", 1),
            ("Both sides should make their case", 3),
            ("Wrong. Prove the claim first 🔍", 5),
        ]},
        {"q": "How did you come to believe in God?", "options": [
            ("God placed it in my heart ❤️", 1),
            ("Upbringing, but I've thought it through since", 3),
            ("I was taught before I could question it 🧠", 5),
        ]},
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
ISLAM_QUESTIONS = {

    "scripture": [
        {"q": "The Quran says the sun sets in a muddy spring (18:86).\n\nThe creator of the universe got where the sun goes wrong?", "options": [("✅ It describes what the traveller saw", 0), ("😐 It's a narrative perspective not cosmology", 1), ("💀 A God who made the universe doesn't know the sun doesn't set in mud", 5)]},
        {"q": "The Quran says the earth is flat and spread out like a carpet (88:20, 2:22).\n\nYour response?", "options": [("✅ It describes the earth from a human perspective", 0), ("😐 Metaphorical language about God's provision", 1), ("💀 The Quran's cosmology is wrong because its authors believed the earth was flat", 5)]},
        {"q": "The Quran describes sperm originating from between the backbone and ribs (86:6-7).\n\nAnatomically that's wrong. Your take?", "options": [("✅ It refers to the origin of the person not the sperm", 0), ("😐 Ancient Arabic has nuanced meanings lost in translation", 1), ("💀 The Quran was written when humans didn't understand their own biology", 5)]},
        {"q": "The Quran says Mary the mother of Jesus is the sister of Aaron (19:28) — who lived 1,400 years earlier.\n\nHistorical error?", "options": [("✅ A different Mary — a title of honour", 0), ("😐 Maryam was a common name and title", 1), ("💀 The author of the Quran confused two people separated by 1,400 years", 5)]},
        {"q": "Allah says he made humans from clay (38:71), from water (21:30), from nothing (19:67), and from a blood clot (96:2).\n\nThese can't all be correct.", "options": [("✅ They describe different aspects of the same creation", 0), ("😐 Different verses emphasise different attributes of creation", 1), ("💀 The Quran contradicts itself on the most basic fact of human creation", 5)]},
        {"q": "The Quran was compiled by humans after Muhammad's death from scraps, bones, and memory. Verses were disputed and some destroyed.\n\nDoes that affect its reliability?", "options": [("✅ God protected its preservation despite human involvement", 0), ("😐 The main text was preserved with exceptional care", 1), ("💀 The history of Quran compilation is not the story of perfect divine preservation", 5)]},
        {"q": "The Quran says Allah created the earth in 2 days, then heavens in 2 days, then returned to earth for 4 more — totalling 8 days.\n\nYet 7:54 says 6 days. Which is right?", "options": [("✅ The numbers represent epochs not literal days", 0), ("😐 The Arabic yawm has flexible meaning", 1), ("💀 God's own book can't agree on how long God took to make the world", 5)]},
        # ── KB additions ──
        {"q": "What's your best evidence that Allah exists?", "options": [
            ("The Quran says so — it's Allah's word 📖", 1),
            ("Personal experience and the universe's design", 3),
            ("A book proving itself is circular reasoning 🔁", 5),
        ]},
        {"q": "The Quran is unfalsifiable — if dua fails it's your lack of faith.\n\nIf it works — Allah did it.\n\nIs that a real test?", "options": [
            ("Faith isn't a test — it's trust 🙏", 1),
            ("The system accounts for human limitation", 3),
            ("Heads I win, tails no faith — still rigged 🎯", 5),
        ]},
    ],

    "hell": [
        {"q": "The Quran says disbelievers will be given boiling water to drink and their skin will be replaced when it melts off — forever (4:56).\n\nIs a God who designed that merciful?", "options": [("😰 God's justice is absolute — disbelievers chose this", 0), ("😐 It emphasises the seriousness of rejecting God", 1), ("💀 The Islamic hell was designed by someone who wanted maximum horror — not maximum justice", 5)]},
        {"q": "There are over 1 billion Muslims. If Islam is the one true religion — what happens to the 7 billion non-Muslims?", "options": [("😐 God judges all by the message they received", 0), ("🤷 Allah's mercy is broader than we understand", 2), ("💀 The numbers alone make Islamic exclusivism morally indefensible", 5)]},
        {"q": "Allah created humans knowing most would go to hell according to Islamic teaching.\n\nWhy create them?", "options": [("🙏 To manifest his attributes of justice and mercy", 0), ("😐 Human choice determines the outcome — not God's design", 1), ("💀 A God who creates people for hell is not merciful by any definition", 5)]},
        {"q": "Muhammad said the majority of people in hell are women (Bukhari 29).\n\nHow do you reconcile that with a just and merciful God?", "options": [("😐 It was about gratitude and ingratitude — not gender condemnation", 0), ("🤔 The hadith says what it says — the explanation feels forced", 2), ("💀 This hadith reflects the misogyny of its author — not divine truth", 5)]},
    ],

    "suffering": [
        {"q": "If Islam is the final and perfect religion — why do Muslim-majority nations rank consistently low on press freedom, gender equality, and human development?", "options": [("😐 Political and historical factors — not religion — explain the rankings", 0), ("🤷 Corruption and colonialism are the cause not Islam", 2), ("💀 A perfect religion producing consistently poor outcomes is worth examining", 5)]},
        {"q": "Some of the most devout Muslims live in extreme poverty.\n\nIs Allah testing them — or has religion taught them to accept what they should be fighting?", "options": [("🙏 Allah tests those he loves most", 0), ("😐 Poverty is a systemic problem not God's fault", 2), ("💀 Teaching the poor to pray instead of organise is the oldest tool of control", 5)]},
        {"q": "Blasphemy laws in Pakistan, Iran, and Saudi Arabia — based on Islamic law — have led to executions.\n\nIs that God's will?", "options": [("😐 Extremists misapply Islamic law", 0), ("🤔 The laws exist in classical Islamic jurisprudence though", 2), ("🔥 Religion that executes critics can't survive honest examination", 5)]},
        # ── KB additions ──
        {"q": "Leaving Islam means losing family and risking safety.\n\nWhat does that say about the faith?", "options": [
            ("Shows how serious the commitment is 🛐", 1),
            ("Harsh, but faith itself can still be valid", 3),
            ("Any belief that punishes exit is a cage 🔓", 5),
        ]},
        {"q": "Studies show religious people report higher satisfaction.\n\nProof that Islam works?", "options": [
            ("Allah gives peace the world can't give 😊", 1),
            ("Helps some people even if not literally true", 3),
            ("Secular nations score highest on wellbeing 📊", 5),
        ]},
        {"q": "Teaching kids they're born with a fitrah yet face jahannam if they stray.\n\nIs that love or harm?", "options": [
            ("It prepares them spiritually — it's love ❤️‍🔥", 1),
            ("Good intention — delivery can hurt though", 3),
            ("Threatening a child with hellfire is abuse 🧠", 5),
        ]},
    ],

    "health": [
        {"q": "Muhammad said the black seed (Nigella sativa) cures all diseases except death.\n\nDoes that claim hold up medically?", "options": [("✅ It has proven medicinal properties — science is catching up", 0), ("😐 All diseases was hyperbole for many diseases", 1), ("💀 A prophet making false medical claims raises questions about all his claims", 5)]},
        {"q": "Muhammad said flies carry disease in one wing and the cure in the other — dip the whole fly in your drink (Bukhari 3320).\n\nWould you do that?", "options": [("✅ It has been validated by modern research on fly antimicrobials", 0), ("😐 This hadith is authentic — I trust the Prophet's knowledge", 1), ("💀 Following this hadith could kill you — not cure you", 5)]},
        {"q": "You got sick. The doctor treated you. You recovered.\n\nWho do you thank — Allah or the doctor?", "options": [("🙏 Allah — he guided the doctor", 0), ("😐 Both deserve gratitude", 2), ("💀 If Allah gets credit for the doctor's work — what exactly does the doctor get?", 5)]},
        # ── KB addition ──
        {"q": "Someone survives illness and says Alhamdulillah — Allah healed them.\n\nYour honest take?", "options": [
            ("Allah heard their dua and healed them 🙏", 1),
            ("Prayer helped their mindset at least", 3),
            ("Doctors saved them. Dua took the credit 🏥", 5),
        ]},
    ],

    "accident": [
        {"q": "You survived a near-fatal accident.\n\nMost Muslims say Alhamdulillah — God saved me.\n\nBut if God chose to save you — he also chose not to save others who died the same day.\n\nIs that fair?", "options": [("🙏 God's plan differs for each soul", 0), ("😐 We can't understand Allah's wisdom", 1), ("💀 Randomness explains accident survival better than divine selection", 5)]},
        {"q": "A devout Muslim dies in a car accident on the way to Friday prayer.\n\nWas that Allah's will?\n\nAnd if yes — what does that say about prayer protecting the faithful?", "options": [("🙏 Death at any moment is Allah's predetermined plan", 0), ("😐 Prayer doesn't guarantee physical safety", 2), ("💀 The idea that God has a plan removes all meaning from tragedy and triumph equally", 5)]},
    ],

    "death": [
        {"q": "If Allah controls when you die — why do Muslims go to hospital?\n\nIf it's your time — nothing can stop it.", "options": [("🙏 We use the means available — Allah decides the outcome", 0), ("😐 Seeking medicine is part of following the Sunnah", 2), ("💀 Seeking medicine is an implicit acknowledgement that prayer alone doesn't determine survival", 5)]},
        {"q": "Every Muslim eventually dies — just like every non-Muslim.\n\nFaith doesn't extend life statistically.\n\nDoes that challenge the idea that Allah rewards the faithful in this life?", "options": [("🙏 Rewards come in the akhirah — not this life", 0), ("😐 Faith isn't about living longer — it's about living better", 2), ("💀 An afterlife reward system that can never be verified is indistinguishable from no reward system", 5)]},
    ],

    "success": [
        {"q": "If someone works hard for years and succeeds without faith — what does that say about Islam being necessary for success?", "options": [("🙏 All success comes from Allah whether they know it or not", 0), ("😐 Worldly success doesn't require faith", 2), ("💀 If success doesn't need God — what role does faith actually play?", 5)]},
        {"q": "Two Muslims make dua for the same thing. One gets it. One doesn't.\n\nHow do you explain that?", "options": [("🙏 Allah answers according to his wisdom not our desires", 0), ("😐 The timing or conditions might differ", 1), ("💀 If prayer outcomes are random — prayer has no reliable function", 5)]},
        {"q": "If a non-believer lives an ethical life and a believer lives a harmful one — who deserves better in this world?", "options": [("🙏 Iman matters more than deeds alone", 0), ("😐 Both iman and deeds matter in Islam", 1), ("💀 A system that values belief over behaviour produces harmful believers", 5)]},
    ],

    "myth": [
        {"q": "Islam spread across Africa, Persia, and Spain largely through military conquest.\n\nDoes a religion of peace spread by the sword?", "options": [("🙏 God uses all means to spread truth", 0), ("😐 Most early religions spread through power", 2), ("💀 Forced conversion is just imperialism with a prayer mat", 5)]},
        {"q": "The concept of abrogation means later Quran verses cancel earlier peaceful ones.\n\nThe later Medina verses are more violent.\n\nWhat does that progression tell you?", "options": [("🙏 God adapted the message to the needs of the growing community", 0), ("😐 Later verses provide legal framework — earlier ones remain spiritually valid", 1), ("💀 The Quran's most violent verses are the ones God decided to keep", 5)]},
        {"q": "Islamic banking prohibits interest yet uses legal workarounds that achieve exactly the same financial outcome.\n\nIs that genuine compliance with God's law?", "options": [("✅ The prohibition is on exploitative usury — Islamic finance avoids that", 0), ("😐 It's a legitimate distinction that matters to God", 1), ("💀 Islamic banking is proof that religious law bends to economic reality", 5)]},
    ],

    "morality": [
        {"q": "Muhammad married Aisha when she was 6 and consummated the marriage when she was 9.\n\nHow do you view that?", "options": [("✅ Different times — different cultural norms", 0), ("😬 Scholars debate the actual age", 1), ("💀 This alone disqualifies Muhammad as a moral exemplar", 5)]},
        {"q": "Quran 4:34 allows men to beat their wives.\n\nHow is that from a God of love?", "options": [("✅ In context it means light tap as a last resort", 0), ("😐 Scholars say it means symbolic gesture", 1), ("💀 That verse was written by a man — not God", 5)]},
        {"q": "Leaving Islam — apostasy — carries the death penalty in many Islamic teachings.\n\nYour view?", "options": [("✅ Faith must be protected from corruption", 0), ("😐 It's a misapplication by extremists", 1), ("🔥 If your religion needs death threats to keep people — it's a prison", 5)]},
        {"q": "The Quran permits sex with female war captives (4:24, 33:50).\n\nHow is that moral?", "options": [("😐 It regulated an existing practice to protect women", 0), ("🤔 I find those verses very difficult", 2), ("💀 The Quran gave divine permission for rape of captives", 5)]},
        {"q": "Muhammad owned slaves and participated in the slave trade.\n\nDoes that affect his status as a moral exemplar?", "options": [("✅ He improved the treatment of slaves significantly for his era", 0), ("😐 Slavery was universal then — he was still ahead of his time", 1), ("💀 The perfect human role model owned and traded human beings", 5)]},
        # ── KB additions ──
        {"q": "Why do you try to be a good person?", "options": [
            ("Allah is watching — I fear judgment 😇", 1),
            ("My faith and genuinely caring for people", 3),
            ("Empathy. Fear of hell isn't real morality ⚖️", 5),
        ]},
        {"q": "Your dua didn't get answered.\n\nWhy?", "options": [
            ("My iman wasn't strong enough 🙏", 1),
            ("Maybe it wasn't Allah's timing", 3),
            ("Prayer doesn't change outcomes 🎯", 5),
        ]},
    ],

    "science": [
        {"q": "Islam teaches the world is only a few thousand years old.\n\nScience confirms it's 4.5 billion years old.\n\nWho's right?", "options": [("✅ Islamic scripture over secular science", 0), ("😐 The Quran doesn't specify an exact age", 2), ("💀 Young earth Islam collapses under the weight of evidence", 5)]},
        {"q": "The Quran describes mountains as pegs holding the earth stable (78:6-7).\n\nGeology shows mountains rise from tectonic movement and CAUSE earthquakes.", "options": [("✅ Mountains do anchor continental plates in a sense", 0), ("😐 The peg metaphor describes their visual appearance", 1), ("💀 The Quran's geology is wrong — mountains do the opposite of stabilise the earth", 5)]},
        {"q": "The Quran describes human embryo development inaccurately — claiming bones form before flesh (23:14).\n\nModern embryology shows they form simultaneously.", "options": [("✅ The Quran's embryology is remarkably advanced for its time", 0), ("😐 Arabic terms have broader meanings than English translations suggest", 1), ("💀 Claiming Quranic embryology is miraculous requires ignoring what it actually says", 5)]},
        # ── KB additions ──
        {"q": "When science and the Quran contradict — which do you trust?", "options": [
            ("The Quran — Allah's word over science 📜", 1),
            ("Depends on the topic, I try to balance both", 3),
            ("Science. It's evidence-based and self-correcting 🔬", 5),
        ]},
        {"q": "A brilliant scientist believes in Allah.\n\nWhat does that prove?", "options": [
            ("Even the smartest recognise Allah is real 🧬", 1),
            ("Smart people hold different beliefs", 3),
            ("Smart people get conditioned too 🎓", 5),
        ]},
    ],

    "hope": [
        {"q": "If someone finds purpose, community, and happiness without Islam — does that challenge the idea that faith is necessary?", "options": [("🙏 True purpose ultimately comes from Allah", 0), ("😐 People can find meaning in different ways", 2), ("💀 If meaning exists without faith — what makes faith necessary?", 5)]},
        {"q": "Muhammad received all his revelations alone with no witnesses.\n\nWhy should anyone believe they were divine?", "options": [("✅ The Quran itself is the miracle — its literary perfection proves it", 0), ("😐 Many prophets received revelation alone", 1), ("💀 Every religion was founded on one person's unverifiable claim", 5)]},
        # ── KB additions ──
        {"q": "Without Allah, what's the point of life?", "options": [
            ("There isn't one — only Allah gives meaning 🌟", 1),
            ("Hard, but people find their own purpose", 3),
            ("Meaning is made, not given from above 🔥", 5),
        ]},
        {"q": "You feel Allah's presence during salah.\n\nWhat does that actually mean?", "options": [
            ("Allah is near — he's communicating with me 🙌", 1),
            ("It feels real — I'm unsure what it is", 3),
            ("My brain did it — same as every religion 🧩", 5),
        ]},
        {"q": "'Prove Allah doesn't exist.' Your reaction?", "options": [
            ("Fair point — you can't disprove him 🤷", 1),
            ("Both sides should make their case", 3),
            ("Wrong. The claim needs proof first 🔍", 5),
        ]},
        {"q": "How did you come to believe in Islam?", "options": [
            ("Allah placed it in my heart ❤️", 1),
            ("Upbringing, but I've thought it through since", 3),
            ("I was taught before I could question it 🧠", 5),
        ]},
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
HINDUISM_QUESTIONS = {
    "scripture": [
        {"q": "The Vedas describe a geocentric universe with the sun revolving around the earth.\n\nScience has conclusively proven otherwise.", "options": [("✅ The Vedas describe a spiritual cosmology not a physical one", 0), ("😐 Ancient metaphorical cosmology shouldn't be evaluated by modern physics", 2), ("💀 The Vedas describe the universe as their human authors believed it was", 5)]},
        {"q": "Hinduism has no single founder, no single scripture, no central authority.\n\nDoes that make it more or less believable as divinely revealed?", "options": [("✅ Its organic development shows it emerged from genuine spiritual experience", 0), ("😐 The diversity shows its universal spiritual truth", 2), ("💀 Hinduism is a collection of tribal practices that accumulated over millennia — not divine revelation", 5)]},
        {"q": "The Rigveda contains hymns praising Soma — an intoxicating substance — as divine.\n\nWhat does that tell you?", "options": [("🙏 Soma represents spiritual transcendence symbolically", 0), ("😐 Ancient ritual substances had different spiritual significance", 2), ("💀 Ancient Hindus got high and called the high God — that's the Rigveda", 5)]},
    ],
    "hell": [
        {"q": "In Hinduism, hell (Naraka) is temporary — souls eventually reincarnate.\n\nDoes a temporary punishment for a lifetime of choices make moral sense?", "options": [("✅ The soul ultimately moves toward moksha — it's merciful", 0), ("😐 Karmic justice is more nuanced than permanent punishment", 2), ("💀 A justice system where everyone eventually gets off has no real accountability", 5)]},
    ],
    "suffering": [
        {"q": "Karma teaches that suffering in this life is the result of actions in a past life.\n\nDoes that mean victims of abuse or poverty deserve it?", "options": [("🙏 Karma is more complex than simple punishment", 0), ("😐 We don't always understand how karma works", 2), ("💀 Karma is victim-blaming dressed in spiritual language", 5)]},
        {"q": "Hinduism places the cow above human beings in many practical applications.\n\nIs an animal more sacred than a human?", "options": [("🙏 The cow represents abundance and non-violence — it's symbolic", 0), ("😐 Sacred doesn't mean more important than humans", 2), ("💀 A religion that protects cows while lower-caste humans starve has its priorities wrong", 5)]},
    ],
    "health": [
        {"q": "Ayurveda recommends drinking cow urine as medicine.\n\nIs that medically sound?", "options": [("✅ Cow urine has antimicrobial properties — science is confirming ancient wisdom", 0), ("😐 It's been used for thousands of years — there's wisdom in tradition", 1), ("💀 Ancient medical practices were guesswork — sanctifying them as divine doesn't make them safe", 5)]},
    ],
    "accident": [
        {"q": "In Hindu belief, your death is predetermined by karma from past lives.\n\nIf that's true — what's the point of wearing a seatbelt?", "options": [("🙏 We follow dharma and use practical wisdom while accepting karma's ultimate role", 0), ("😐 Dharma includes taking care of your body", 2), ("💀 People who believe in predetermined fate still wear seatbelts because deep down they don't actually believe it", 5)]},
    ],
    "death": [
        {"q": "Reincarnation — the soul cycling through millions of births — has no scientific evidence.\n\nWhat makes you believe it?", "options": [("✅ Some people remember past lives — that's evidence", 0), ("😐 It's a metaphysical truth beyond material evidence", 2), ("💀 Reincarnation is a comforting story with zero verifiable evidence", 5)]},
        {"q": "Moksha — liberation from rebirth — is the ultimate goal of Hindu life.\n\nBut no one who has achieved it has come back to confirm it.\n\nHow do you know it's real?", "options": [("🙏 Great sages have described the state of liberation", 0), ("😐 Its truth is beyond empirical verification", 2), ("💀 Moksha is a beautiful idea for which there is no evidence whatsoever", 5)]},
    ],
    "success": [
        {"q": "The caste system assigns your life's work at birth.\n\nCan effort and merit overcome a divinely ordained social position?", "options": [("✅ Karma from past lives explains — not limits — your current position", 0), ("😐 Modern Hinduism has moved away from rigid caste restrictions", 2), ("💀 The caste system is the most efficient success prevention system ever invented", 5)]},
    ],
    "myth": [
        {"q": "The dying-and-rising god pattern — Osiris, Dionysus, Mithras, Krishna, Jesus — all follow the same template.\n\nWhat does that tell you about religious mythology?", "options": [("🙏 Cultures pointed to the same divine truth", 0), ("😐 Universal archetypes reflect deep human spiritual experience", 2), ("💀 Religious stories follow human storytelling templates because they were written by humans", 5)]},
    ],
    "morality": [
        {"q": "Hinduism's caste system divides humans by birth into hierarchies.\n\nThe lowest — Dalits — were considered untouchable.\n\nIs that divinely ordained?", "options": [("✅ It reflects karmic justice from past lives", 0), ("😐 The spiritual caste system was corrupted by humans", 2), ("💀 The caste system is religious discrimination institutionalised as cosmic law", 5)]},
        {"q": "Multiple Hindu texts describe women as inherently inferior and requiring male guardianship at all stages of life.\n\nIs that divine truth?", "options": [("😐 Those texts reflect cultural context — not divine hierarchy", 0), ("🤔 The texts are consistent enough to suggest it wasn't just culture", 3), ("💀 Every major religion's founding texts were written by men who believed women were inferior", 5)]},
    ],
    "science": [
        {"q": "Hinduism teaches the universe cycles through Yugas — the current Kali Yuga lasting 432,000 years.\n\nIs that compatible with what we know about cosmic history?", "options": [("✅ The Yuga system describes spiritual not purely physical cycles", 0), ("😐 It's a cosmological framework that shouldn't be compared to material science", 2), ("💀 Cosmic cycles were invented by people with no knowledge of actual cosmology", 5)]},
    ],
    "hope": [
        {"q": "Yoga, meditation, and Ayurveda have measurable benefits that work even for non-believers.\n\nDoes that mean the benefits come from the practice — not from Hinduism?", "options": [("🙏 The spiritual technology works because of its divine origin", 0), ("😐 The benefits are real regardless of the framework", 3), ("💀 Yoga is a physical and mental practice — its effectiveness has nothing to do with Brahman", 5)]},
    ],
}

# ═══════════════════════════════════════════════════════════════════════════════
# SMART SAMPLING — ensures category spread in every test
# ═══════════════════════════════════════════════════════════════════════════════

CATEGORIES = ["scripture", "hell", "suffering", "health", "accident",
               "death", "success", "myth", "morality", "science", "hope"]


def get_religion_questions(religion: str, n: int = 15) -> list:
    """
    Pull questions ensuring at least one from each category.
    Remaining slots filled randomly from the full pool.
    """
    if religion == "christianity":
        bank = CHRISTIANITY_QUESTIONS
    elif religion == "islam":
        bank = ISLAM_QUESTIONS
    elif religion == "hinduism":
        bank = HINDUISM_QUESTIONS
    elif religion == "both":
        half = n // 2
        c_qs = _spread_sample(CHRISTIANITY_QUESTIONS, half)
        i_qs = _spread_sample(ISLAM_QUESTIONS, n - half)
        combined = c_qs + i_qs
        random.shuffle(combined)
        return combined
    else:
        merged = {}
        for cat in CATEGORIES:
            merged[cat] = (
                CHRISTIANITY_QUESTIONS.get(cat, []) +
                ISLAM_QUESTIONS.get(cat, []) +
                HINDUISM_QUESTIONS.get(cat, [])
            )
        return _spread_sample(merged, n)

    return _spread_sample(bank, n)


def _spread_sample(bank: dict, n: int) -> list:
    """Sample n questions with at least 1 from each available category."""
    result = [] 

    # Step 1 — take one from each available category
    shuffled_cats = list(CATEGORIES)
    random.shuffle(shuffled_cats)

    for cat in shuffled_cats:
        if len(result) >= n:
            break
        pool = bank.get(cat, [])
        if pool:
            result.append(random.choice(pool))

    # Step 2 — fill remaining slots from full pool
    full_pool = [q for cat_qs in bank.values() for q in cat_qs]
    already = set(id(q) for q in result)
    remaining = [q for q in full_pool if id(q) not in already]
    random.shuffle(remaining)

    slots_left = n - len(result)
    result.extend(remaining[:slots_left])

    # Step 3 — shuffle so categories aren't grouped
    random.shuffle(result)
    return result[:n]