#1278787753:AAFcLjwUUZRE0qgPpNIJreo8cV5AHILTS64
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import telegram.error
import csv
import pandas as pd

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

updater = Updater(token='1278787753:AAFcLjwUUZRE0qgPpNIJreo8cV5AHILTS64', use_context=True)

dispatcher = updater.dispatcher
#----------------------------------------------------------
df1 = pd.read_csv("Links_That_Need_To_Give_Engagment.csv")
#------------------------------------------------------------
def start(update, context):

    keyboard = [
        [
            InlineKeyboardButton("📷 Picture 📷", url = update.message.text), #when not url it sends error
        ],
        [
            InlineKeyboardButton("👥 More Groups 👥", url = "https://taplink.cc/wandering.loop/p/3c6800/"),
            InlineKeyboardButton("💎 Premium 💎", url = "https://taplink.cc/wandering.loop")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="✅ Dx42  \n👤 Name: {}\n👥 User Name: {}\n🔗 Link: {} ".format(
                                 update.message.from_user.first_name, update.message.from_user.username,
                                 update.message.text),
                             reply_markup=reply_markup, disable_web_page_preview = True)

    context.bot.deleteMessage(chat_id=df1["Link_Chat_Id"], message_id= df1["Link_Message_Id"])




dispatcher.add_handler(MessageHandler(Filters.text, start))#i dont want a hancelers

updater.start_polling()
