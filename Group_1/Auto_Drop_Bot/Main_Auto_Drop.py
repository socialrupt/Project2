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

File_Save = "Group_1/Group1_Autodrop.csv"

Get_Posts_Miniutes_Ago = 10
Group_Username_From_CSV = "@{}".format(pd.read_csv("Group_1/Group1_Global_Settings.csv")["Group_Username"].iloc[0])
#--------------------


L = instaloader.Instaloader()



Bot_With_Token = telegram.Bot(token= pd.read_csv("Group_1/Group1_Global_Settings.csv")["Autodrop_Bot_Key"].iloc[0])
while True:
    print(DT.now())
    print(111)
    time.sleep(60 * 10)
    Usernames_From_CSV = pd.read_csv(File_Save)
    df11 = pd.read_csv(File_Save)

    SINCE = DT.now() - timedelta(minutes=Get_Posts_Miniutes_Ago)
    UNTIL = DT.now()
    for index, row in Usernames_From_CSV.iterrows():
        print(222)
        Target_UserName = row["IG_Username"]
        AutoDrop_Num_Today123 = row["AutoDrop_Num_Today"]
        AutoDrop_Limit_Per_Day123 = row["AutoDrop_Limit_Per_Day"]

        now = datetime.datetime.now().time()
        if now.hour == 00 and now.minute == 00:#Resets the daily count of drops
            df11.loc[index, "AutoDrop_Num_Today"] = 0
            df11.to_csv(File_Save, index=False)
            print("!!!")
        else:
            pass

        if int(AutoDrop_Limit_Per_Day123) > int(AutoDrop_Num_Today123):
            print(333)
            posts = instaloader.Profile.from_username(L.context, Target_UserName[1:]).get_posts()
#the page must have astleast one post for this to work
            for post in posts:
                break

            if post.date_local > SINCE:
                if post.date_local <= UNTIL:
                    print(444)


                    def Send_AutoDrop_URL_To_Group1():
                        keyboard = [
                            [
                                InlineKeyboardButton("📷 Picture 📷",
                                                     url="https://www.instagram.com/p/{}/".format(post.shortcode)),
                                # when not url it sends error
                            ],
                            [
                                InlineKeyboardButton("👥 More Groups 👥", url="https://taplink.cc/wandering.loop/p/3c6800/"),
                                InlineKeyboardButton("💎 Premium 💎", url="https://taplink.cc/wandering.loop")
                            ],
                        ]

                        reply_markup = InlineKeyboardMarkup(keyboard)

                        Bot_With_Token.sendMessage(chat_id=Group_Username_From_CSV,
                                                   text="✅ Dx42\n🔗 Link: https://www.instagram.com/p/{}/ ".format(
                                                       str(post.shortcode)), reply_markup=reply_markup,
                                                   disable_web_page_preview=True)


                    df11 = pd.read_csv(File_Save)
                    df11.loc[index, "AutoDrop_Num_Today"] = AutoDrop_Num_Today123 + 1
                    df11.to_csv(File_Save, index=False)
                    Send_AutoDrop_URL_To_Group1()

                else:

                    print("Not the recent post2")
                    continue #why do we need break?
            else:

                print("Not the recent post1")
                continue

        else:
            print("Hit the max limit of day")
            continue

#The code is basiclly looping over ALL the fucking posts from an accoun and then will go to the next account.