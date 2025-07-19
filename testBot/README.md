# Telegram Bot Example

A simple Telegram bot built with Python using the `python-telegram-bot` library. This bot can echo messages, greet users, provide inspirational quotes, and more. Easily extendable with new commands.

## Features
- Echoes user messages
- /start — Welcome message
- /help — List available commands
- /greet — Greet the user
- /quote — Get a random inspirational quote

## Setup Instructions

### 1. Clone the repository
```sh
git clone https://github.com/irenkamalova/testBot.git
cd testBot
```

### 2. Create a virtual environment (recommended)
```sh
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Create a Telegram Bot and get the token
- Talk to [@BotFather](https://t.me/BotFather) on Telegram
- Use `/newbot` to create a new bot and get your API token

### 5. Set your bot token as an environment variable
```sh
export TELEGRAM_BOT_TOKEN=your_token_here
```
On Windows (cmd):
```cmd
set TELEGRAM_BOT_TOKEN=your_token_here
```

### 6. Run the bot
```sh
python bot.py
```

## How to Add New Commands
1. Define a new async function in `bot.py` for your command. Example:
    ```python
    async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message:
            await update.message.reply_text('This is my new command!')
    ```
2. Register the command handler in the `if __name__ == '__main__':` block:
    ```python
    app.add_handler(CommandHandler('mycommand', my_command))
    ```
3. Add a description to the `/help` command if desired.

## Contribution Guidelines
- Fork the repository and create your branch from `main`.
- Add your feature or fix.
- Ensure code is clean and documented.
- Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 