#1278787753:AAFcLjwUUZRE0qgPpNIJreo8cV5AHILTS64
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import time


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

updater = Updater(token='1278787753:AAFcLjwUUZRE0qgPpNIJreo8cV5AHILTS64', use_context=True)

dispatcher = updater.dispatcher
#You need to find a way to echo instagram links only and delete other messages.
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Working")

dispatcher.add_handler(MessageHandler(Filters.text, start))

updater.start_polling()


