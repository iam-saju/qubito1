from telegram.ext import Updater, CommandHandler
import logging

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram Bot API token
TOKEN = '7073224449:AAFsOirg8-rvhNTZrOTTmjECxRJ2KAfUISA'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the /start command handler
def start(update, context):
    user_id = update.effective_user.id
    context.bot.send_message(chat_id=user_id, text="Hello! I am your bot. How can I assist you today?")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()
    logging.info("Bot started polling...")
    updater.idle()

if __name__ == '__main__':
    main()
