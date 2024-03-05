# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import requests
import config
import ticketCheck
import time

config = config.Config()
bot_token = config.bot_token
bot_chatIDs = config.bot_chatIDs

# send message to certain user
# bot_chatIDs = '<array of chat_ids>'
# bot_token = '<token str>'
def tgbot_send_message(bot_token, bot_chatID, bot_message):
    bot_token = bot_token
    bot_chatID = bot_chatID
    bot_message = bot_message
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text('echo: {}'.format(update.message.text))

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Continuously check the ticket status and send a message when sold out
    while True:
        # 檢查售票狀態，並回傳
        ticket_status = ticketCheck.main()
        # ticket check, if ticket is soldable return 1, else return 0
        print(ticket_status)
        if ticket_status[0] == 0:
            '''bot_message = ""
            [tgbot_send_message(bot_token, chat_id, bot_message) for chat_id in bot_chatIDs]'''
            # 當下沒票就間隔五分鐘再檢查一次
            time.sleep(290)
            continue
        else:
            bot_message = '‼️有票了，快手刀去買‼️\nlink: https://chimeimuseum.fonticket.com/ticket/earlybird\n\n{}'.format(ticket_status)
            # send alarm message to users by tg bot
            [tgbot_send_message(bot_token, chat_id, bot_message) for chat_id in bot_chatIDs]
            # 有票還是繼續跑，但是沒有間隔，有票期間就一直傳（？吵到你去買票
            time.sleep(0)
            continue
        
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()