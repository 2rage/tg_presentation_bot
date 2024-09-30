import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from frontend import run_flask_server, add_question
from threading import Thread

load_dotenv()

questions = []


async def start(update: Update, context):
    await update.message.reply_text("Привет! Задайте свой вопрос.")


async def handle_question(update: Update, context):
    question = update.message.text
    add_question(question)
    await update.message.reply_text(f'Ваш вопрос "{question}" был добавлен.')


def run_telegram_bot():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        print("Ошибка: Токен не найден в .env")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question))

    app.run_polling()


def main():

    flask_thread = Thread(target=run_flask_server)
    flask_thread.start()

    run_telegram_bot()


if __name__ == "__main__":
    main()
