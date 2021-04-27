
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import telegram.error
import csv
import pandas as pd
def Main_Ting():
    Bot_With_Token = telegram.Bot(token= pd.read_csv("Group_1/Group1_Global_Settings.csv")["Leeching_Bot_Key"].iloc[0])

    df1 = pd.read_csv("Group_1/Leeching_Bot/Warning file test.csv").tail(1)
    df2 = pd.read_csv("Group_1/Leeching_Bot/Links_That_Need_To_Give_Engagment.csv")
    df3 = pd.read_csv("Group_1/Group1_Settings.csv")
    df4 = pd.read_csv("Group_1/Leeching_Bot/Leached_Posts.csv")

    for Loop_Over_User_Id_From_CSV in df2["Link_User_Id"]:
        if str(df3.loc[0]["Warning_Status"]).upper() == "ON":
            Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV), text="You have not fully engaged. \nYou have been warned!!!")

            Num_Lines_Looped_Over = 0
            try:
                if len(df4["Leached_Likes"].dropna()) > 0:
                    for I in df4["Leached_Likes"].dropna():
                        print(df4["Leached_Likes"].dropna(), "lllllllllll")
                        Num_Lines_Looped_Over += 1
                        Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV),
                                                   text="https://instagram.com/p/{}/ Like Required ❌".format(I),
                                                   disable_web_page_preview=True)

                        if Num_Lines_Looped_Over == len(df4["Leached_Likes"].dropna()):
                            print(df4["Leached_Comments"].dropna())
                            Num_Lines_Looped_Over = 0
                            for I in df4["Leached_Comments"].dropna():
                                Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV),
                                                           text="https://instagram.com/p/{}/ Comment Required ❌".format(
                                                               I), disable_web_page_preview=True)


                        else:
                            pass
                elif len(df4["Leached_Likes"].dropna()) == 0:
                    # The code below dosnt requre the same elif statment as the likes block of code becuase LIKES LEACH goes first.
                    for I in df4["Leached_Comments"].dropna():
                        Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV),
                                                   text="https://instagram.com/p/{}/ Comment Required ❌".format(I),
                                                   disable_web_page_preview=True)


            finally:

                filename = "Group_1/Leeching_Bot/Leached_Posts.csv"
                f = open(filename, "w+")
                writer = csv.writer(f)
                writer.writerow(["Leached_Comments", "Leached_Likes"])
                f.close()

        elif str(df3.loc[0]["Warning_Status"]).upper() == "OFF":
            Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV), text="You have not fully engaged.")


            Num_Lines_Looped_Over = 0
            try:
                if len(df4["Leached_Likes"].dropna()) > 0:
                    for I in df4["Leached_Likes"].dropna():
                        print(df4["Leached_Likes"].dropna(), "lllllllllll")
                        Num_Lines_Looped_Over += 1
                        Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV),
                                                   text="https://instagram.com/p/{}/ Like Required ❌".format(I), disable_web_page_preview=True)

                        if Num_Lines_Looped_Over == len(df4["Leached_Likes"].dropna()):
                            print(df4["Leached_Comments"].dropna())
                            Num_Lines_Looped_Over = 0
                            for I in df4["Leached_Comments"].dropna():
                                Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV),text="https://instagram.com/p/{}/ Comment Required ❌".format(I), disable_web_page_preview=True)


                        else:
                            pass
                elif len(df4["Leached_Likes"].dropna()) == 0:
                    #The code below dosnt requre the same elif statment as the likes block of code becuase LIKES LEACH goes first.
                    for I in df4["Leached_Comments"].dropna():
                        Bot_With_Token.sendMessage(chat_id=str(Loop_Over_User_Id_From_CSV),
                                                   text="https://instagram.com/p/{}/ Comment Required ❌".format(I),
                                                   disable_web_page_preview=True)


            finally:

                filename = "Group_1/Leeching_Bot/Leached_Posts.csv"
                f = open(filename, "w+")
                writer = csv.writer(f)
                writer.writerow(["Leached_Comments", "Leached_Likes"])
                f.close()
        else:
            pass
