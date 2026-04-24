import logging, os, asyncio
from datetime import time as dtime
from telegram import (Update, InlineKeyboardButton, InlineKeyboardMarkup,
                      InlineQueryResultArticle, InputTextMessageContent)
from telegram.ext import (Application, CommandHandler, MessageHandler,
                           filters, ContextTypes, CallbackQueryHandler,
                           ConversationHandler, InlineQueryHandler)
from agent import AtheismAgent
from prompts import (WELCOME_MESSAGE, HELP_MESSAGE, TOPICS_MESSAGE, get_tone_prompt,
                     ATHEISM_SYSTEM_PROMPT, DEEP_DIVE_PROMPT, REACTIONS, GREETINGS)
from matrix_prompts import (MATRIX_SYSTEM_PROMPT, get_matrix_tone_prompt,
                             get_matrix_result, MATRIX_WELCOME, MATRIX_DEEP_DIVE_PROMPT)
from config import TELEGRAM_BOT_TOKEN
from questions_bank import get_religion_questions
from matrix_questions import get_matrix_questions
from referral import (get_referral_link, record_referral,
                      get_referral_count, is_unlocked, UNLOCK_THRESHOLD)
from daily_broadcast import broadcast
from image_card import generate_result_card
from onboarding import (is_onboarded, complete_onboarding,
                        increment_interactions, get_tone, get_religion,
                        save_mode, get_mode, save_location, get_location,
                        has_both_tests, can_switch_mode)
from analytics import (track_user, track_message, track_faith_test,
                       track_matrix_test, get_stats, get_recent_users)
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
BOT_USERNAME  = os.getenv("BOT_USERNAME", "mirror_bot")
BROADCAST_CH  = os.getenv("BROADCAST_CHANNEL", "")
ADMIN_ID      = int(os.getenv("ADMIN_ID", "0"))

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

print("\n=== Starting Mirror Bot ===\n")
agent = AtheismAgent()

SELECT_MODE, SELECT_RELIGION, QUESTION = range(3)

RELIGION_MAP = {
    "christianity": ("Christianity ✝️", 10),
    "islam":        ("Islam ☪️", 10),
    "hinduism":     ("Hinduism 🕉️", 10),
    "both":         ("Christianity + Islam", 20),
    "all":          ("All Religions 🌍", 30),
}

def mode_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛐 Know Your Faith", callback_data="mode_faith")],
        [InlineKeyboardButton("🔴 Know the Matrix", callback_data="mode_matrix")],
    ])

def religion_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✝️ Christianity",  callback_data="rel_christianity")],
        [InlineKeyboardButton("☪️ Islam",         callback_data="rel_islam")],
        [InlineKeyboardButton("🕉️ Hinduism",      callback_data="rel_hinduism")],
        [InlineKeyboardButton("✝️ + ☪️ Both",     callback_data="rel_both")],
        [InlineKeyboardButton("🌍 All Religions", callback_data="rel_all")],
    ])

def build_keyboard(qi, options):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(opt[0], callback_data=f"{qi}:{opt[1]}")]
        for opt in options
    ])

def faith_result(score, total):
    pct = round((score / (total * 5)) * 100)
    if pct <= 15:   label,emoji,desc = "True Believer","🙏","You trust your faith fully.\n\nTee respects the commitment — even if he disagrees with every bit of it."
    elif pct <= 35: label,emoji,desc = "Faithful but Curious","🤔","You believe, but cracks are forming.\n\nDangerous territory — once you start asking, it's hard to stop."
    elif pct <= 55: label,emoji,desc = "On the Fence","😐","Half in, half out.\n\nYou're the agnostic who hasn't fully admitted it yet."
    elif pct <= 75: label,emoji,desc = "Closet Atheist","👀","You don't really believe anymore.\n\nYou just haven't said it out loud yet."
    elif pct <= 90: label,emoji,desc = "Proud Atheist","😤","Logic runs your life, not scripture.\n\nYou might stay quiet at family dinners — but inside you are done."
    else:           label,emoji,desc = "Full Antitheist","🔥","You don't just disbelieve — you think religion is actively harmful.\n\nHitchens would be proud."
    bar = "█"*(pct//10) + "░"*(10-pct//10)
    return pct, label, emoji, desc, bar

def matrix_result(score, total):
    pct = round((score / (total * 5)) * 100)
    label, emoji, desc = get_matrix_result(pct)
    bar = "█"*(pct//10) + "░"*(10-pct//10)
    return pct, label, emoji, desc, bar

def faith_tone_from_pct(pct):
    if pct <= 30: return "gentle"
    elif pct <= 65: return "analytical"
    else: return "provocative"

def matrix_tone_from_pct(pct):
    if pct <= 40: return "gentle"
    elif pct <= 70: return "analytical"
    else: return "strategic"

# ── /start ─────────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args

    if args and args[0].startswith("ref_"):
        try:
            ref_id = int(args[0].replace("ref_", ""))
            if ref_id != user.id:
                record_referral(ref_id)
                if get_referral_count(ref_id) >= UNLOCK_THRESHOLD:
                    await context.bot.send_message(
                        chat_id=ref_id,
                        text="🔓 *Deep Dive unlocked!* Type /deepdive.",
                        parse_mode="Markdown")
        except Exception:
            pass

    track_user(user.id, user.username, user.first_name)

    already_tested = context.user_data.get("onboarded", False) or is_onboarded(user.id)

    if already_tested:
        await update.message.reply_text(
            f"Welcome back {user.first_name} 👋\n\n"
            "Want to take another test or keep chatting?",
            parse_mode="Markdown",
            reply_markup=mode_keyboard()
        )
    else:
        await update.message.reply_text(
            f"Hey {user.first_name} 👋\n\n"
            "*Welcome to Take the Red Pill.* 🔴\n\n"
            "Two tests. One truth.\n\n"
            "🛐 *Know Your Faith* — how religious are you really?\n"
            "🔴 *Know the Matrix* — how aware are you of your own life?\n\n"
            "Take a test first — it tells me how to talk to you.\n\n"
            "Pick one to start:",
            parse_mode="Markdown",
            reply_markup=mode_keyboard()
        )
    return SELECT_MODE

# ── Mode selection ─────────────────────────────────────────────────────────────

async def select_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    mode = query.data.replace("mode_", "")
    context.user_data["mode"] = mode
    context.user_data["onboarded"] = True
    save_mode(update.effective_user.id, mode)

    if mode == "faith":
        await query.edit_message_text(
            "🛐 *Know Your Faith*\n\nPick a religion to focus on:",
            parse_mode="Markdown",
            reply_markup=religion_keyboard()
        )
        return SELECT_RELIGION
    else:
        questions = get_matrix_questions(20)
        context.user_data.update({
            "score": 0, "step": 0,
            "questions": questions, "total": len(questions)
        })
        await query.edit_message_text(MATRIX_WELCOME, parse_mode="Markdown")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"*Question 1 of {len(questions)}*\n\n{questions[0]['q']}",
            parse_mode="Markdown",
            reply_markup=build_keyboard(0, questions[0]["options"])
        )
        return QUESTION

# ── Religion selection ─────────────────────────────────────────────────────────

async def select_religion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    religion = query.data.replace("rel_", "")
    label, n = RELIGION_MAP.get(religion, ("All Religions", 30))
    questions = get_religion_questions(religion, n)
    context.user_data.update({
        "score": 0, "step": 0, "religion": religion,
        "questions": questions, "total": len(questions)
    })
    await query.edit_message_text(
        f"⚡ *{label} Test*\n\n{n} questions. Be honest 😏",
        parse_mode="Markdown"
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"*Question 1 of {n}*\n\n{questions[0]['q']}",
        parse_mode="Markdown",
        reply_markup=build_keyboard(0, questions[0]["options"])
    )
    return QUESTION

# ── Answer handler ─────────────────────────────────────────────────────────────

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data.startswith("rel_") or query.data.startswith("mode_"):
        return QUESTION

    try:
        qi, points = query.data.split(":")
        qi, points = int(qi), int(points)
    except Exception:
        return QUESTION

    if context.user_data.get("step", 0) != qi:
        return QUESTION

    questions = context.user_data.get("questions", [])
    context.user_data["score"] = context.user_data.get("score", 0) + points
    next_qi = qi + 1
    context.user_data["step"] = next_qi

    if next_qi < len(questions):
        await query.edit_message_text(
            f"*Question {next_qi+1} of {len(questions)}*\n\n{questions[next_qi]['q']}",
            parse_mode="Markdown",
            reply_markup=build_keyboard(next_qi, questions[next_qi]["options"])
        )
        return QUESTION

    # ── Test complete ──────────────────────────────────────────────────────────
    score  = context.user_data["score"]
    total  = context.user_data["total"]
    mode   = context.user_data.get("mode", "faith")
    user   = update.effective_user
    uname  = user.username or user.first_name or "anonymous"

    if mode == "matrix":
        pct, label, emoji, desc, bar = matrix_result(score, total)
        tone = matrix_tone_from_pct(pct)
        track_matrix_test(user.id, label, pct, tone)
        closing = {
            "gentle":     "Ask me anything — I'll start easy and build up.",
            "analytical": "Ready to go deeper? Ask me anything.",
            "strategic":  "You already see the game. Let's sharpen the strategy. 🔴",
        }.get(tone, "Ask me anything.")

        # Leaderboard
        s = get_stats()
        total_tests = s.get("total_matrix_tests", 0)
        leaderboard_line = ""
        if total_tests and total_tests > 5:
            order_matrix = ["Asleep","Waking Up","Aware","Strategic","Fully Unplugged"]
            bd = s.get("matrix_breakdown", {})
            idx_l = order_matrix.index(label) if label in order_matrix else 0
            below = sum(bd.get(l, 0) for l in order_matrix[:idx_l+1])
            pct_rank = max(5, min(95, round((below / total_tests) * 100)))
            leaderboard_line = f"\n\n📊 You scored higher than *{pct_rank}%* of people who took this test."

        result_text = (
            f"*Your Matrix Score: {label} {emoji}*\n\n"
            f"{bar}  *{pct}%*\n\n"
            f"{desc}\n\n"
            f"_{closing}_"
            f"{leaderboard_line}\n\n"
            f"🔗 /referral  ⭐ /donate"
        )
        card_subtitle = "Know the Matrix"
    else:
        religion = context.user_data.get("religion", "all")
        pct, label, emoji, desc, bar = faith_result(score, total)
        tone = faith_tone_from_pct(pct)
        complete_onboarding(user.id, religion, score, total, label)
        track_faith_test(user.id, label, pct, religion, tone)
        closing = {
            "gentle":      "Curious about something? Just ask — I'll start easy 😊",
            "analytical":  "Ready to go deeper? Ask me anything.",
            "provocative": "You already know the game. Zero filter from here. 🔥",
        }.get(tone, "Ask me anything.")

        # Leaderboard
        s = get_stats()
        total_tests = s.get("total_faith_tests", 0)
        leaderboard_line = ""
        if total_tests and total_tests > 5:
            order_faith = ["True Believer","Faithful but Curious","On the Fence","Closet Atheist","Proud Atheist","Full Antitheist"]
            bd = s.get("faith_breakdown", {})
            idx_l = order_faith.index(label) if label in order_faith else 0
            below = sum(bd.get(l, 0) for l in order_faith[:idx_l+1])
            pct_rank = max(5, min(95, round((below / total_tests) * 100)))
            leaderboard_line = f"\n\n📊 You scored higher than *{pct_rank}%* of people who took this test."

        result_text = (
            f"*Your Faith Score: {label} {emoji}*\n\n"
            f"{bar}  *{pct}%*\n\n"
            f"{desc}\n\n"
            f"_{closing}_"
            f"{leaderboard_line}\n\n"
            f"🔗 /referral  ⭐ /donate"
        )
        card_subtitle = "Know Your Faith"

    context.user_data["last_pct"]   = pct
    context.user_data["last_label"] = label
    context.user_data["last_tone"]  = tone

    # Save to agent profile
    profile_update = {
        "username": uname,
        f"{mode}_label": label,
        f"{mode}_score": pct,
        f"{mode}_tone": tone,
    }
    if mode == "faith":
        profile_update["faith_religion"] = context.user_data.get("religion", "all")
    agent.set_user_profile(user.id, profile_update)

    await query.edit_message_text(result_text, parse_mode="Markdown")

    # Auto card
    try:
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="upload_photo")
        card = await generate_result_card(
            context.bot, user.id, uname, pct, label, subtitle=card_subtitle)
        other_mode = "Matrix 🔴" if mode == "faith" else "Faith 🛐"
        await context.bot.send_photo(
            chat_id=update.effective_chat.id, photo=card,
            caption=(
                f"*{label}* — {pct}%\n\n"
                f"📸 Screenshot and share — tag @teetheredpill\n\n"
                f"Want to try the *{other_mode} test* too? Type /test"
            ),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Card: {e}")

    # Ask for location after first test if not set
    try:
        loc = get_location(user.id)
        if not loc.get("country"):
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=(
                    "🌍 One quick thing — where are you from?\n\n"
                    "Just type your country or city.\n"
                    "I use it to make examples more relevant to you.\n\n"
                    "_(You can also do this anytime with /location)_"
                ),
                parse_mode="Markdown"
            )
            context.user_data["awaiting_location"] = True
    except Exception:
        pass

    # Preserve awaiting_location across the clear
    ask_location = context.user_data.get("awaiting_location", False)
    context.user_data.clear()
    context.user_data["onboarded"] = True
    context.user_data["mode"] = mode
    context.user_data["last_tone"] = tone
    if ask_location:
        context.user_data["awaiting_location"] = True
    return ConversationHandler.END

async def cancel_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    context.user_data["onboarded"] = True
    await update.message.reply_text("Test cancelled. Type /start to choose a mode.")
    return ConversationHandler.END

# ── Commands ───────────────────────────────────────────────────────────────────

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*Commands:*\n\n"
        "/start — Choose a mode\n"
        "/test — Retake a test\n"
        "/mode — Check your current mode\n"
        "/switch — Switch between Faith and Matrix\n"
        "/location — Set your location for personalised examples\n"
        "/help — This menu\n"
        "/reset — Clear conversation\n"
        "/topics — What Tee knows\n"
        "/referral — Your invite link\n"
        "/deepdive — Unlock uncensored mode\n"
        "/donate — Support the bot\n\n"
        "*Modes:*\n"
        "🛐 Know Your Faith — religion test\n"
        "🔴 Know the Matrix — life awareness test\n\n"
        "📢 Join the channel: @teetheredpill",
        parse_mode="Markdown"
    )

async def topics_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not context.user_data.get("onboarded", False) and not is_onboarded(user.id):
        await update.message.reply_text("Take the test first 👉 /start")
        return
    await update.message.reply_text(TOPICS_MESSAGE, parse_mode="Markdown")

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    mode = context.user_data.get("mode") or get_mode(user.id)
    agent.reset_history(user.id, mode)
    await update.message.reply_text(
        f"Cleared {'Matrix' if mode == 'matrix' else 'Faith'} history. 🧹 What's on your mind?"
    )

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Which test do you want to take?",
        reply_markup=mode_keyboard()
    )
    return SELECT_MODE

async def referral_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    link = get_referral_link(BOT_USERNAME, user.id)
    count = get_referral_count(user.id)
    rem = max(0, UNLOCK_THRESHOLD - count)
    status = "🔓 *Deep Dive unlocked!* /deepdive" if is_unlocked(
        user.id) else f"Need *{rem} more* to unlock."

    # Personalised challenge using last test result
    profile = agent.get_user_profile(user.id)
    fl = profile.get("faith_label")
    fs = profile.get("faith_score")
    ml = profile.get("matrix_label")
    ms = profile.get("matrix_score")

    if fl and fs:
        challenge = (
            f"\n\n_Forward this to someone:_\n"
            f"_I just scored {fs}% on the Faith test 🔴_\n"
            f"_They called me {fl} 😏_\n"
            f"_Think you can beat me? →_ {link}"
        )
    elif ml and ms:
        challenge = (
            f"\n\n_Forward this to someone:_\n"
            f"_I just scored {ms}% on the Matrix test 🔴_\n"
            f"_They called me {ml} 😏_\n"
            f"_Think you can beat me? →_ {link}"
        )
    else:
        challenge = f"\n\n_Send this to a friend:_\n_Take the Red Pill test → {link}_"

    await update.message.reply_text(
        f"🔗 *Your referral link:*\n`{link}`\n\n"
        f"Friends joined: *{count}/{UNLOCK_THRESHOLD}*\n\n"
        f"{status}\n\n"
        f"When {UNLOCK_THRESHOLD} friends join the *Deep Dive* unlocks."
        f"{challenge}",
        parse_mode="Markdown"
    )

async def deepdive_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_unlocked(update.effective_user.id):
        count = get_referral_count(update.effective_user.id)
        link = get_referral_link(BOT_USERNAME, update.effective_user.id)
        await update.message.reply_text(
            f"🔒 *Deep Dive locked.*\n\nNeed *{UNLOCK_THRESHOLD-count} more* friends.\n\n`{link}`",
            parse_mode="Markdown")
        return
    agent.set_user_profile(update.effective_user.id, {"deep_dive": True})
    await update.message.reply_text(
        "🔥 *Deep Dive — Zero Filter Unlocked*\n\n"
        "You earned this.\n\n"
        "Ask me anything:\n"
        "• How Islam actually spread by the sword\n"
        "• The men who wrote the Bible and why\n"
        "• Why African religion is a colonial wound that never healed\n"
        "• Scientology and what it reveals about ALL religion\n"
        "• The sexual politics buried in both holy books\n"
        "• Life traps most people never escape\n\n"
        "Zero filter. Go ahead. 🔴",
        parse_mode="Markdown"
    )

async def donate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⭐ *Support Take the Red Pill*\n\n"
        "If this bot made you think — or made your religious friend angry — it did its job. 😏\n\n"
        "Support keeps it running, ad-free, and unfiltered.\n\n"
        "*How to send Telegram Stars:*\n"
        "1. Tap the attachment icon (📎) in this chat\n"
        "2. Select ⭐ Stars\n"
        "3. Choose an amount and send\n\n"
        "Or share the bot with one person who needs the red pill. That counts too. 🔴\n\n"
        "👉 t.me/honestteebot",
        parse_mode="Markdown"
    )

async def mode_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    mode = context.user_data.get("mode") or get_mode(user.id)
    other = "matrix" if mode == "faith" else "faith"
    other_name = "Know the Matrix 🔴" if other == "matrix" else "Know Your Faith 🛐"
    mode_name = "Know Your Faith 🛐" if mode == "faith" else "Know the Matrix 🔴"
    can_switch = can_switch_mode(user.id)

    if can_switch:
        switch_text = f"✅ You can switch.\n\nType /switch to move to *{other_name}*"
    else:
        switch_text = (
            f"🔒 To switch you need to complete *both tests* first.\n\n"
            f"You haven't taken the *{other_name}* test yet.\n"
            f"Type /test to take it."
        )
    await update.message.reply_text(
        f"*Current mode: {mode_name}*\n\n"
        f"All your messages are answered in this mode.\n\n"
        f"{switch_text}",
        parse_mode="Markdown"
    )

async def switch_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    mode = context.user_data.get("mode") or get_mode(user.id)

    if not can_switch_mode(user.id):
        other = "Know the Matrix 🔴" if mode == "faith" else "Know Your Faith 🛐"
        await update.message.reply_text(
            f"🔒 *Mode switching is locked.*\n\n"
            f"Take the *{other}* test first.\n\nType /test to begin.",
            parse_mode="Markdown"
        )
        return

    new_mode = "matrix" if mode == "faith" else "faith"
    new_name = "Know the Matrix 🔴" if new_mode == "matrix" else "Know Your Faith 🛐"
    context.user_data["mode"] = new_mode
    context.user_data["last_tone"] = "analytical"
    save_mode(user.id, new_mode)

    await update.message.reply_text(
        f"✅ *Switched to {new_name}*\n\n"
        f"All your messages will now be answered in this mode.\n\n"
        f"Type /mode anytime to check or switch again.",
        parse_mode="Markdown"
    )

async def location_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 *Where are you from?*\n\n"
        "Just type your country or city — I'll use it to make examples more relevant to you.\n\n"
        "Example: _Nigeria_, _Ghana_, _Israel_, _Mecca_, _United States_, _Lagos Nigeria_, _Texas US_",
        parse_mode="Markdown"
    )
    context.user_data["awaiting_location"] = True

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if ADMIN_ID and update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("🔒 Admin only.")
        return
    s = get_stats()
    if "error" in s:
        await update.message.reply_text(f"Error: {s['error']}")
        return
    faith_bd   = "\n".join(f"  {k}: {v}" for k,v in sorted(s.get("faith_breakdown",{}).items(), key=lambda x:-x[1]))
    matrix_bd  = "\n".join(f"  {k}: {v}" for k,v in sorted(s.get("matrix_breakdown",{}).items(), key=lambda x:-x[1]))
    religion_bd= "\n".join(f"  {k}: {v}" for k,v in sorted(s.get("religion_breakdown",{}).items(), key=lambda x:-x[1]))
    recent = get_recent_users(5)
    recent_text = "\n".join(
        f"  • {u.get('first_name','?')} | Faith:{u.get('faith_last_score','?')}% | Matrix:{u.get('matrix_last_score','?')}%"
        for u in recent
    )
    total_tests = s.get("total_faith_tests",0) + s.get("total_matrix_tests",0)
    await update.message.reply_text(
        f"📊 *Take the Red Pill — Stats*\n"
        f"━━━━━━━━━━━━━━━\n\n"
        f"👥 Total users: *{s['total_users']}*\n"
        f"🆕 New today: *{s['new_today']}*\n"
        f"📅 Active 7 days: *{s['active_7d']}*\n"
        f"💬 Total messages: *{s['total_messages']}*\n\n"
        f"🧪 Total tests: *{total_tests}*\n"
        f"🛐 Faith tests: *{s['total_faith_tests']}*\n"
        f"🔴 Matrix tests: *{s['total_matrix_tests']}*\n"
        f"🔥 Deep Dive unlocked: *{s.get('deep_dive_unlocked', 0)}*\n\n"
        f"*Faith breakdown:*\n{faith_bd or '  none yet'}\n\n"
        f"*Matrix breakdown:*\n{matrix_bd or '  none yet'}\n\n"
        f"*Religion picks:*\n{religion_bd or '  none yet'}\n\n"
        f"*Recent users:*\n{recent_text or '  none yet'}",
        parse_mode="Markdown"
    )

# ── Message handler ────────────────────────────────────────────────────────────

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg  = update.message.text.strip()
    low  = msg.lower().rstrip("!?.")

    track_user(user.id, user.username, user.first_name)
    track_message(user.id)

    # ── LOCATION INPUT — must be checked FIRST before anything else ───────────
    if context.user_data.get("awaiting_location"):
        context.user_data["awaiting_location"] = False
        parts = msg.split(",")
        country = parts[-1].strip() if len(parts) > 1 else msg.strip()
        city    = parts[0].strip() if len(parts) > 1 else ""
        save_location(user.id, country, city)
        agent.set_user_profile(user.id, {"country": country, "city": city})
        loc_display = f"{city}, {country}" if city else country
        await update.message.reply_text(
            f"✅ Got it — *{loc_display}* 🌍\n\n"
            f"I'll use that for examples from now on.",
            parse_mode="Markdown"
        )
        return

    # ── ONBOARDING GATE ───────────────────────────────────────────────────────
    already_tested = context.user_data.get("onboarded", False) or is_onboarded(user.id)
    if not already_tested:
        await update.message.reply_text(
            "Hey 👋 Take the test first — it tells me how to talk to you.\n\nType /start to begin 🔴"
        )
        return

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    # ── RESTORE MODE ──────────────────────────────────────────────────────────
    saved_mode = get_mode(user.id)
    mode = context.user_data.get("mode") or saved_mode
    if saved_mode and saved_mode != "faith":
        mode = saved_mode
    context.user_data["mode"] = mode
    tone = context.user_data.get("last_tone", "analytical")
    logger.info(f"[{user.first_name}] mode={mode} tone={tone}")

    # ── SYNC LOCATION to agent ────────────────────────────────────────────────
    loc = get_location(user.id)
    if loc.get("country"):
        agent.set_user_profile(user.id, {
            "country": loc["country"],
            "city": loc.get("city", "")
        })

    # ── BUILD SYSTEM PROMPT ───────────────────────────────────────────────────
    user_profile  = agent.get_user_profile(user.id)
    has_deep_dive = user_profile.get("deep_dive", False) or is_unlocked(user.id)

    if mode == "matrix":
        base_system = (
            "YOU ARE IN: KNOW THE MATRIX MODE\n"
            "DO NOT discuss religion, God, Islam, Christianity, or faith.\n"
            "You are a life strategist and mentor. Focus ONLY on life awareness, "
            "social conditioning, time, purpose, success, and mindset.\n\n"
            + MATRIX_SYSTEM_PROMPT + "\n\n" + get_matrix_tone_prompt(tone)
        )
        if has_deep_dive:
            base_system += "\n\n" + MATRIX_DEEP_DIVE_PROMPT
    else:
        base_system = (
            "YOU ARE IN: KNOW YOUR FAITH MODE\n"
            "Focus on religion, God, Islam, Christianity, Hinduism, and related philosophy.\n\n"
            + ATHEISM_SYSTEM_PROMPT + "\n\n" + get_tone_prompt(tone)
        )
        if has_deep_dive:
            base_system += "\n\n" + DEEP_DIVE_PROMPT

    # ── GREETING ─────────────────────────────────────────────────────────────
    if low in GREETINGS:
        if agent.has_history(user.id, mode):
            topic = agent.get_last_topic_summary(user.id, mode)
            short = topic[:60] + "..." if len(topic) > 60 else topic
            await update.message.reply_text(
                f"Hey 👋\n\nWe were talking about: _{short}_\n\nWant to continue?",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text("Hey 👋 What's on your mind?")
        return

    # ── REACTION / SHORT REPLY ────────────────────────────────────────────────
    if low in REACTIONS or len(msg.split()) <= 4:
        last = agent.get_last_bot_message(user.id, mode)
        if last:
            short_ctx = last[:300] + "..." if len(last) > 300 else last
            prompt = (
                f"The user replied '{msg}' to what you just said.\n"
                f"Your last message was: '{short_ctx}'\n\n"
                f"Continue building on EXACTLY that point. "
                f"Don't switch topics. Acknowledge their reaction first, "
                f"then go one layer deeper. Keep it short and punchy."
            )
            reply = agent.chat_with_system(user.id, prompt, system_override=base_system, mode=mode)
            await _send(update, reply)
            return

    # ── NORMAL MESSAGE ────────────────────────────────────────────────────────
    profile = increment_interactions(user.id)
    new_tone = profile.get("tone", tone)
    if new_tone != tone:
        context.user_data["last_tone"] = new_tone
        if mode == "matrix":
            base_system = (
                "YOU ARE IN: KNOW THE MATRIX MODE\n"
                "DO NOT discuss religion, God, Islam, Christianity, or faith.\n\n"
                + MATRIX_SYSTEM_PROMPT + "\n\n" + get_matrix_tone_prompt(new_tone)
            )
        else:
            base_system = (
                "YOU ARE IN: KNOW YOUR FAITH MODE\n\n"
                + ATHEISM_SYSTEM_PROMPT + "\n\n" + get_tone_prompt(new_tone)
            )

    reply = agent.chat_with_system(user.id, msg, system_override=base_system, mode=mode)
    await _send(update, reply)

async def _send(update: Update, text: str):
    try:
        if len(text) <= 4096:
            await update.message.reply_text(text, parse_mode="Markdown")
        else:
            for i in range(0, len(text), 4000):
                await update.message.reply_text(text[i:i+4000], parse_mode="Markdown")
    except Exception:
        await update.message.reply_text(text[:4096] if len(text) > 4096 else text)

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.inline_query.answer([
        InlineQueryResultArticle(
            id="1", title="Share Take the Red Pill 🔴",
            description="Know Your Faith + Know the Matrix",
            input_message_content=InputTextMessageContent(
                f"🔴 Take the Red Pill test → t.me/{BOT_USERNAME}\n\n"
                f"Know Your Faith + Know the Matrix 😏"
            )
        ),
    ], cache_time=10)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Error: {context.error}")

async def daily_job(context: ContextTypes.DEFAULT_TYPE):
    await broadcast(context.bot)

# ── Main ───────────────────────────────────────────────────────────────────────

async def run_bot():
    if not TELEGRAM_BOT_TOKEN:
        print("[ERROR] TELEGRAM_BOT_TOKEN not found"); return

    keep_alive()
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            CommandHandler("test",  test_command),
        ],
        states={
            SELECT_MODE:     [CallbackQueryHandler(select_mode,    pattern="^mode_")],
            SELECT_RELIGION: [CallbackQueryHandler(select_religion, pattern="^rel_")],
            QUESTION:        [CallbackQueryHandler(handle_answer)],
        },
        fallbacks=[CommandHandler("cancel", cancel_test)],
        per_message=False, per_chat=True, allow_reentry=True,
    )

    app.add_handler(conv)
    for cmd, fn in [
        ("help",     help_command),
        ("reset",    reset_command),
        ("topics",   topics_command),
        ("referral", referral_command),
        ("deepdive", deepdive_command),
        ("donate",   donate_command),
        ("stats",    stats_command),
        ("mode",     mode_command),
        ("switch",   switch_command),
        ("location", location_command),
    ]:
        app.add_handler(CommandHandler(cmd, fn))

    app.add_handler(InlineQueryHandler(inline_query))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)

    if BROADCAST_CH:
        try:
            if app.job_queue:
                app.job_queue.run_daily(daily_job, time=dtime(9, 0, 0))
                print(f"[OK] Daily broadcast → {BROADCAST_CH}")
            else:
                print("[WARN] JobQueue not available")
        except Exception as e:
            print(f"[WARN] Broadcast error: {e}")

    print("Take the Red Pill bot is live.\n")
    async with app:
        await app.start()
        await app.updater.start_polling(allowed_updates=Update.ALL_TYPES)
        await asyncio.Event().wait()
        await app.updater.stop()
        await app.stop()

def main():
    import time
    retry = 0
    print("[START] Take the Red Pill bot starting...")
    while True:
        try:
            print(f"[RUN] Starting bot loop (attempt {retry + 1})")
            asyncio.run(run_bot())
        except KeyboardInterrupt:
            print("\n[STOP] Stopped by user.")
            break
        except Exception as e:
            retry += 1
            wait = min(30, 3 * retry)
            print(f"[CRASH] {type(e).__name__}: {e}")
            print(f"[RETRY] Restarting in {wait}s...")
            time.sleep(wait)
        else:
            print("[EXIT] Bot exited cleanly — restarting...")
            time.sleep(3)

if __name__ == "__main__":
    import time
    main()