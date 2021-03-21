"""
This code checks if the user is a current effecnder or not.
if they are have leached before then they will there status will be updated.
If they have not leached before then they will get there user id added to the csv.

"""

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import csv
import pandas as pd
from telegram import ChatPermissions
def Main_Ting():
    #----------------------
    File_Save = "Warning file test.csv"
    Num_Of_Times_Warned = 0
    #----------------------
    updater = Updater(token= pd.read_csv("../Group1_Global_Settings.csv")["Leeching_Bot_Key"].iloc[0], use_context=True)

    dispatcher = updater.dispatcher

    df1 = pd.read_csv("Links_That_Need_To_Give_Engagment.csv")
    df2 = pd.read_csv("Warning file test.csv")
    df3 = pd.read_csv("../Group1_Settings.csv")
    #---------------------------------------------------------
    if str(df3.loc[0]["Warning_Status"]).upper() == "ON":

        for Loop_Over_Links_ChatID in reversed(df1["Link_Chat_Id"]): #Loops over the Give file to get the values
            for Loop_Over_UserIDs in reversed(df1["Link_User_Id"]):
                for Loop_Over_Users_Warning in reversed(df2["Warns"]):
                    for Loop_Over_User_IDs_From_Warningfile in reversed(df2["User_id"]):

                        Links_Dropped_By_User_UserID = Loop_Over_UserIDs
                        Links_Dropped_By_User_Chat_Id = Loop_Over_Links_ChatID
                        Warns_From_File = Loop_Over_Users_Warning
                        User_ID_From_Warning_File = Loop_Over_User_IDs_From_Warningfile

                        if Links_Dropped_By_User_UserID == User_ID_From_Warning_File:#Checks if the leacher is a new effender or old
                            if Warns_From_File == 1 and Num_Of_Times_Warned == 0 or Warns_From_File == 2 and Num_Of_Times_Warned == 0:
                                Num_Of_Times_Warned += 1
                                Colunm_To_Check = "User_id"
                                Colunm_To_Update = "Warns"
                                Value_To_Identify_Row = Links_Dropped_By_User_UserID  # Set this to the user_id of the leacher.
                                # -----------------------------------------------------#I don't know how this code works
                                index = df2.index
                                condition = df2[Colunm_To_Check] == Value_To_Identify_Row
                                indices = index[condition]

                                indices_list = indices.tolist()  # This var gives the index


                                for Take_Value_Out_Of_List in indices_list:  # This take the value out of the list
                                    pass
                                # ----------------------------------------

                                df2.at[Take_Value_Out_Of_List, Colunm_To_Update] += 1  # Identifyies and increments the value


                                df2.to_csv(File_Save, index=False)

                                import Send_Warning_To_Group
                                Send_Warning_To_Group.Main_Ting()

                                break
        #=============================================================================================================

                            elif Warns_From_File >= int(df3.loc[0]["NumWarns"]): #Attack the code bro

                                if str(df3.loc[0]["Warning_Punishment"]).upper() == "BAN":

                                    updater.bot.kick_chat_member(str(Loop_Over_Links_ChatID), str(Loop_Over_UserIDs))

                                    df1 = pd.read_csv("Warning file test.csv")
                                    df2 = df1[df1.User_id != Links_Dropped_By_User_UserID]
                                    df2.to_csv("Warning file test.csv", index=False)

                                elif str(df3.loc[0]["Warning_Punishment"]).upper() == "MUTE":

                                    Leacher_Muted = ChatPermissions(can_send_messages = False, can_send_media_messages = False, can_send_polls = False, can_send_other_messages = False, can_add_web_page_previews = False, can_change_info = False, can_invite_users = False, can_pin_messages = False)
                                    updater.bot.restrict_chat_member(str(Loop_Over_Links_ChatID), str(Loop_Over_UserIDs), permissions= Leacher_Muted)

                                    df1 = pd.read_csv("Warning file test.csv")
                                    df2 = df1[df1.User_id != Links_Dropped_By_User_UserID]
                                    df2.to_csv("Warning file test.csv", index=False)

                                else:
                                    pass
                            else:
                                pass

                        else:#There has to be at least 1 line of values for this to work
                            Duplicate_Rows = []
                            for Check_UserID in df2["User_id"]:
                                if Check_UserID == Loop_Over_UserIDs:
                                    Duplicate_Rows.append(Check_UserID)

                            if Num_Of_Times_Warned == 0 and len(Duplicate_Rows) == 0:
                                Num_Of_Times_Warned += 1
                                with open(File_Save, 'a+', newline='') as write_obj:
                                    csv_writer = csv.writer(write_obj)
                                    csv_writer.writerow([Links_Dropped_By_User_UserID, Links_Dropped_By_User_Chat_Id, 1])
                                import Send_Warning_To_Group
                                Send_Warning_To_Group.Main_Ting()
                                break
                            else:
                                pass
    elif str(df3.loc[0]["Warning_Status"]).upper() == "OFF":
        import Send_Warning_To_Group
        Send_Warning_To_Group.Main_Ting()

    else:
        print("problem!!!!!!!!!!!!!")


