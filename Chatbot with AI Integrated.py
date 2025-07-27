# ai_mental_health_bot.py
import openai
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ── 1. keys ─────────────────────────────────────────────────────────
TELEGRAM_TOKEN = "8276251614:AAGA-uP_gipiy_QzEnhhj4Ax1CG2DAXf1Pw"
openai.api_key = "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"  # direct embed (not recommended for prod)

# ── 2. command handlers ─────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm your AI mental‑health companion 🤖💚\n"
        "Type /ask <your message> to chat with me."
    )

async def ask_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("❗ Please type something after /ask")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    "You are a kind, supportive mental‑health companion. "
                    "Reply with empathy, practical tips, and encouragement."
                )},
                {"role": "user", "content": prompt},
            ],
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Sorry, the AI service failed: {e}"

    await update.message.reply_text(reply)

# ── 3. main ─────────────────────────────────────────────────────────
def main() -> None:
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask_ai))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ask_ai))  # optional: free‑text fallback

    app.run_polling()

if __name__ == "__main__":
    main()
