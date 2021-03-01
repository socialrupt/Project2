
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import telegram.error
import csv
import pandas as pd
def Main_Ting():
    Bot_With_Token = telegram.Bot(token='1556820797:AAH172KNLitYDHfdyPMLanWyJnK5xuGrVx8')

    df1 = pd.read_csv("Warning file test.csv").tail(1)
    df2 = pd.read_csv("Links_That_Need_To_Give_Engagment.csv")
    df3 = pd.read_csv("../Group1_Settings.csv")
    df4 = pd.read_csv("Leached_Posts.csv")

    for Loop_Over_User_Id_From_CSV in df2["Link_User_Id"]:
        if str(df3.loc[0]["Warning_Status"]).upper() == "ON":
            Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV), text="You have not fully engaged. \nYou have been warned!!!")

            break
        elif str(df3.loc[0]["Warning_Status"]).upper() == "OFF":
            Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV), text="You have not fully engaged.")

            for I in df4["Leached_Likes"]:
                print(I, "lollllllllllllllllllllllllllllllllllllllllllll")
                if str(I) != "nan":
                    Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV),text = "https://www.instagram.com/{}/".format(I))
                elif str(I) == "nan":
                    for I in df4["Leached_Comments"]:
                        Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV),text="https://www.instagram.com/{}/".format(I))
                else:
                    print("This should never run!!")
