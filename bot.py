import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your bot.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text('Available commands:\n/start - Welcome message\n/help - Show this help message\n/greet - Greet the user\n/quote - Get a random inspirational quote')

async def greet_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.effective_user:
        user_first_name = update.effective_user.first_name or "there"
        await update.message.reply_text(f'Hello, {user_first_name}!')

async def quote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [
        "The best way to get started is to quit talking and begin doing. – Walt Disney",
        "Don’t let yesterday take up too much of today. – Will Rogers",
        "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
        "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
        "Success is not in what you have, but who you are. – Bo Bennett",
        "The harder you work for something, the greater you’ll feel when you achieve it."
    ]
    if update.message:
        await update.message.reply_text(random.choice(quotes))

if __name__ == '__main__':
    if not TOKEN:
        print('Please set the TELEGRAM_BOT_TOKEN environment variable.')
        exit(1)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('greet', greet_command))
    app.add_handler(CommandHandler('quote', quote_command))
    print('Bot is running...')
    app.run_polling() 