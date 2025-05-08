from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7896304787:AAEfX96bA8ePTabLq_PYw7LHw5EtO4CsSSI"  # Замените на реальный токен

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("после победы или проигрыша перезапусти бота")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()