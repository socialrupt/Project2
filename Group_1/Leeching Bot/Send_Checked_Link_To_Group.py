from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import telegram.error
import csv
import pandas as pd

def Main_ting():
    Bot_With_Token = telegram.Bot(token= pd.read_csv("../Group1_Global_Settings.csv")["Leeching_Bot_Key"].iloc[0])

    df1 = pd.read_csv("Links_That_Need_To_Be_Sent_To_Group.csv")
    df2 = pd.read_csv("Links_That_Need_To_Give_Engagment.csv")



    for IG_Links_From_CSV in df1["Links"]:
        for Chat_IDs_From_CSV in df1["Link_Chat_Id"]:

            keyboard = [
                [
                    InlineKeyboardButton("📷 Picture 📷", url="https://www.instagram.com/p/{}/".format(IG_Links_From_CSV)),  # when not url it sends error
                ],
                [
                    InlineKeyboardButton("👥 More Groups 👥", url="https://taplink.cc/wandering.loop/p/3c6800/"),
                    InlineKeyboardButton("💎 Premium 💎", url="https://taplink.cc/wandering.loop")
                ],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            Bot_With_Token.sendMessage(chat_id=Chat_IDs_From_CSV, text="✅ Dx42\n🔗 Link: https://www.instagram.com/p/{}/ ".format(str(IG_Links_From_CSV)), reply_markup=reply_markup, disable_web_page_preview = True)


