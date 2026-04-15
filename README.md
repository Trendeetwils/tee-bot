# Atheism AI Telegram Bot
### A RAG-powered Telegram bot specialized in atheism, secular philosophy & freethought

---

## FILES IN THIS PROJECT

```
tee-telegram-bot/
├── .env.example          ← Rename to .env and fill in your keys
├── requirements.txt      ← All Python dependencies
├── config.py             ← Settings and configuration
├── prompts.py            ← System prompt and bot messages
├── knowledge_loader.py   ← Loads PDFs, text files, and web pages
├── vector_store.py       ← Builds and loads the ChromaDB vector database
├── agent.py              ← Core AI agent logic (RAG + Claude)
├── telegram_bot.py       ← Main bot — run this to start
├── books/                ← Put your PDF books here
└── texts/                ← Puts your .txt files here
```

---

## STEP-BY-STEP SETUP GUIDE

---

### STEP 1 — Install Python

Make sure Python 3.10 or higher is installed.

Check: `python --version`

If not installed, download from: https://www.python.org/downloads/

---

### STEP 2 — Install dependencies

Open your terminal in this folder and run:

```bash
pip install -r requirements.txt
```

This installs: LangChain, ChromaDB, Anthropic SDK, python-telegram-bot, and more.

---

### STEP 3 — Get your API keys

**A) Anthropic API Key (for Claude AI)**
1. Go to https://console.anthropic.com
2. Sign up or log in
3. Click "API Keys" → "Create Key"
4. Copy the key (starts with sk-ant-)

**B) Telegram Bot Token (from BotFather)**
1. Open Telegram
2. Search for @BotFather
3. Type /newbot
4. Enter a name for your bot (e.g. "Atheism Philosophy Bot")
5. Enter a username (must end in "bot", e.g. "atheism_phil_bot")
6. BotFather gives you a token like: 1234567890:AAFxxxxxxxxxxxxxxxxxxxxxxxxx
7. Copy that token

---

### STEP 4 — Set up your .env file

1. Rename `.env.example` to `.env`
2. Open `.env` and fill in:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
TELEGRAM_BOT_TOKEN=1234567890:AAFyour-token-here
```

---

### STEP 5 — Add your knowledge base (OPTIONAL but recommended)

Create two folders in this directory:

```bash
mkdir books
mkdir texts
```

Then place your files inside:

**books/** → PDF versions of atheism books:
- The God Delusion (Dawkins)
- God Is Not Great (Hitchens)
- The End of Faith (Sam Harris)
- Why I Am Not a Christian (Russell)
- Breaking the Spell (Dennett)

**texts/** → Any plain .txt files with atheism content:
- Articles, essays, debate transcripts
- Notes you've written on atheist philosophy

You can find free PDFs legally at:
- https://www.gutenberg.org (Russell's works are public domain)
- https://infidels.org/library/

NOTE: If you skip this step, the bot still works using Claude's built-in knowledge.

---

### STEP 6 — Build the vector database

Run this ONCE to process and embed your documents:

```bash
python vector_store.py
```

This will:
- Load all your PDFs and text files
- Scrape web pages from Stanford Encyclopedia of Philosophy
- Create embeddings and save them to ./atheism_vectordb/

This may take 5–15 minutes depending on how many files you have.
You only need to run this once (or again if you add new files).

---

### STEP 7 — Start the Telegram bot

```bash
python telegram_bot.py
```

You should see:
```
=== Starting Atheism AI Telegram Bot ===
[OK] Vector store loaded — RAG is active
Bot token loaded. Starting polling...
Bot is running! Press Ctrl+C to stop.
```

Now open Telegram, find your bot, and send /start.

---

## BOT COMMANDS

| Command | Description |
|---------|-------------|
| /start  | Welcome message |
| /help   | Show all commands |
| /topics | Show what the bot knows |
| /reset  | Clear your conversation history |

---

## RUNNING 24/7 (Deployment)

To keep your bot running permanently, use one of these options:

**Option A — Free: Railway.app**
1. Go to https://railway.app
2. Connect your GitHub repo
3. Add environment variables (ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN)
4. Deploy — it runs forever

**Option B — Free: Render.com**
1. Go to https://render.com
2. Create a new "Background Worker"
3. Set start command: `python telegram_bot.py`
4. Add your environment variables
5. Deploy

**Option C — VPS (DigitalOcean, Hetzner, etc.)**
```bash
# Install screen to keep it running after you disconnect
sudo apt install screen
screen -S atheism-bot
python telegram_bot.py
# Press Ctrl+A then D to detach
```

---

## ADDING MORE KNOWLEDGE

To add new books or articles later:
1. Place new PDFs in books/ or text in texts/
2. Re-run: `python vector_store.py`
3. Restart the bot: `python telegram_bot.py`

---

## TROUBLESHOOTING

**"TELEGRAM_BOT_TOKEN not found"**
→ Make sure .env.example was renamed to .env (no .example at the end)

**"Invalid Anthropic API key"**
→ Check your API key at https://console.anthropic.com

**Bot doesn't respond**
→ Make sure the bot is running (terminal should show "Bot is running!")
→ Try sending /start first

**Slow responses**
→ Normal — Claude takes 3-10 seconds to generate a reply

---

## CUSTOMIZING THE BOT

To change the bot's personality or knowledge focus, edit `prompts.py`:
- `ATHEISM_SYSTEM_PROMPT` — the bot's expertise and behavior rules
- `WELCOME_MESSAGE` — what users see on /start
- `HELP_MESSAGE` — the /help text

---

Built with: Python · LangChain · ChromaDB · Anthropic Claude · python-telegram-bot
# tee-bot
