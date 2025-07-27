from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# Your Bot Token from BotFather
BOT_TOKEN = BOT_TOKEN = "8276251614:AAGA-uP_gipiy_QzEnhhj4Ax1CG2DAXf1Pw"


# Mental health responses
responses = {
    "stress": [
        "I'm sorry to hear you're feeling stressed. Try taking a few deep breaths.",
        "Would you like to talk about what's causing your stress?",
        "Taking breaks and resting your mind can really help with stress."
    ],
    "sad": [
        "It's okay to feel sad sometimes. I'm here for you.",
        "Would you like to share what's making you feel this way?",
        "Talking to a friend or journaling might help you feel better."
    ],
    "anxiety": [
        "Anxiety can feel overwhelming. You're not alone.",
        "Do you want to talk about what's making you anxious?",
        "Try grounding techniques like the 5-4-3-2-1 method to calm your mind."
    ],
    "default": [
        "I'm here to listen. Tell me more about what's on your mind.",
        "That sounds important. How does it make you feel?",
        "Can you explain that a bit more?"
    ]
}

def get_response(message: str) -> str:
    message = message.lower()
    for keyword in responses:
        if keyword in message:
            return random.choice(responses[keyword])
    return random.choice(responses["default"])

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! I'm your AI Mental Health Chatbot. Just type how you're feeling.")

# Main message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    bot_response = get_response(user_message)
    await update.message.reply_text(bot_response)

# Main function to start the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
