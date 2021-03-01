import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import telegram.error
import csv
import pandas as pd
import sys



updater = Updater(token='1556820797:AAH172KNLitYDHfdyPMLanWyJnK5xuGrVx8', use_context=True)
j = updater.job_queue
dispatcher = updater.dispatcher

#-------------------------------------------------
DX_Num = pd.read_csv("../Group1_Settings.csv")["DxNum"].iloc[0]
File_Save = "Links_That_Need_To_Give_Engagment.csv"
#-------------------------------------------------

#------------------------------------------------



def Get_Links(update, context):
    try:
        DX_Num = pd.read_csv("../Group1_Settings.csv")["DxNum"].iloc[0]
        df1 = pd.read_csv("Links_That_Need_To_Get_Engagment.csv")
        Links_Sent = 0
        for Loop_Over_Links in df1["Links"].tail(DX_Num):
            Links_Sent += 1
            context.bot.send_message(chat_id=update.message.from_user.id, text="{}. https://instagram.com/p/{} ".format(Links_Sent,Loop_Over_Links),disable_web_page_preview = True)

        context.bot.send_message(chat_id=update.message.chat.id,
                                     text="Links Have Been Sent To You Privatly.",
                                     disable_web_page_preview=True)
    except telegram.error.Unauthorized:
        context.bot.send_message(chat_id=update.message.chat.id,
                                     text="Please start me and then try again...",
                                     disable_web_page_preview=True)


def Start_Leaching_Proccess(update, context):

    Links_Dropped_By_User = update.message.text
    Links_Dropped_By_User_Chat_Id = update.message.chat.id
    Links_Dropped_By_User_Message_Id = update.message.message_id
    Links_Dropped_By_User_User_Id = update.message.from_user.id
    Links_Dropped_By_User_UserName = update.message.from_user.username

    updater.bot.delete_message(chat_id=Links_Dropped_By_User_Chat_Id, message_id=Links_Dropped_By_User_Message_Id)

    Bot_Not_Inisiated = []

    try:
        context.bot.send_message(chat_id=update.message.from_user.id,
                                 text="Checking your link...")#checks if the user has started the bot.
    except telegram.error.Unauthorized:
        Bot_Not_Inisiated.append(1)


    if len(Bot_Not_Inisiated) == 0:
        if len(Links_Dropped_By_User) == 40:
            d = {'Links': [Links_Dropped_By_User[28:-1]], 'Link_Chat_Id': [Links_Dropped_By_User_Chat_Id], #How do other groups make sure it is a link
                 'Link_Message_Id': [Links_Dropped_By_User_Message_Id], 'Link_User_Id': [Links_Dropped_By_User_User_Id], 'User_Name': [Links_Dropped_By_User_UserName]}

            df = pd.DataFrame(data=d, )

            df.to_csv(File_Save, index=False)

            df2 = pd.read_csv("../Group1_Settings.csv")["FollowAdmins_Status"]
            print(df2)
            if "ON" in str(df2).upper():
                import Check_Following_Admins
                Check_Following_Admins.Main_Ting()

            else:
                import Like_Checker
                Like_Checker.Main_Ting()
                import Comment_Checker
                Comment_Checker.Main_Ting()

        else:
            context.bot.send_message(chat_id=update.message.chat.id,
                                         text="Please use the correct format.\n E.G. https://www.instagram.com/p/CODE/",
                                         disable_web_page_preview=True)

    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text="test test test test...",
                                 disable_web_page_preview=True)

dispatcher.add_handler(CommandHandler("Get_Links", Get_Links))
dispatcher.add_handler(MessageHandler(Filters.chat_type.groups, Start_Leaching_Proccess))


updater.start_polling()
