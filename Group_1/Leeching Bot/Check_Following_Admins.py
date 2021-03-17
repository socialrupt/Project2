import instaloader
from datetime import datetime as DT
from datetime import timedelta
import datetime
from itertools import dropwhile, takewhile
from instaloader import Post
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import telegram.error
import csv
import pandas as pd
import time

def Main_Ting():

    L = instaloader.Instaloader()

    USER = str(pd.read_csv("../../Instagram_accounts.csv")["AdminFollowing_Bot_Username"].iloc[0])
    PASSWORD = str(pd.read_csv("../../Instagram_accounts.csv")["AdminFollowing_Bot_Password"].iloc[0])
    L.login(USER, PASSWORD)

    df1 = pd.read_csv("Links_That_Need_To_Give_Engagment.csv")
    #df1["Links"].iloc[0]
    post = Post.from_shortcode(L.context, str(df1["Links"].iloc[0]))
    Username_Of_Owner = post.owner_username

    print(Username_Of_Owner)

    Following = instaloader.Profile.from_username(L.context, Username_Of_Owner).get_followees()
    df2 = pd.read_csv("../Group1_Admins_IG.csv", skiprows= 1)["UserNames"]

    Num_Of_Admins_Following = 0
    Num_Of_Admins_Not_Following = 0
    Num_Of_Admins_Usernames = len(df2)
    Reminder_Messages_Sent = 0
    Comment_Checker_Activated = 0 #Stops the comment checker to run more than once

    for i in Following:
        for x in df2:
            print(str(x)[1:])

            if str(x)[1:] in str(i):
                Num_Of_Admins_Following += 1

            elif Num_Of_Admins_Following == Num_Of_Admins_Usernames and Comment_Checker_Activated == 0:#Checks their link becuase they are following all admins
                Comment_Checker_Activated += 1

                import Like_Checker
                Like_Checker.Main_Ting()

                import Comment_Checker
                Comment_Checker.Main_Ting()



            elif Num_Of_Admins_Not_Following > 0 and Reminder_Messages_Sent == 0 and Comment_Checker_Activated == 0: #Remind the user privately that they need to follow all admins
                Reminder_Messages_Sent += 1
                Bot_With_Token = telegram.Bot(token= pd.read_csv("../Group1_Global_Settings.csv")["Leeching_Bot_Key"].iloc[0])
                Bot_With_Token.sendMessage(chat_id=str(df1["Link_User_Id"].iloc[0]),
                                           text="@{} You MUST follow all the admins on Instagram before posting a link".format(df1["User_Name"].iloc[0]))
                Bot_With_Token.sendMessage(chat_id=str(df1["Link_User_Id"].iloc[0]),
                                           text="{}".format(df2.to_string(header = False, index = False)))#TEST THISSSSSSSSSS
            else:#Runs when they are not folowing a admin
                Num_Of_Admins_Not_Following += 1
                print("Not following this admin")
