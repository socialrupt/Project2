from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

import pandas as pd
import csv


Waiting_For_User_Choice, \
Waiting_For_Choice_Group1_Settings, \
Waiting_For_User_Choice_in_Group1_Premium_Settings, \
Waiting_For_UserName_To_Add_in_Group1_Premium_Settings, \
Waiting_For_UserName_To_Kick_in_Group1_Premium_Settings, \
Waiting_For_Number_in_Group1_GroupFormat_Settings, \
Waiting_For_User_Choice_in_Group1_AutoDrop_Settings, \
Waiting_For_UserName_To_Add_in_Group1_AutoDrop_Settings, \
Waiting_For_Limit_To_Add_in_Group1_AutoDrop_Settings, \
Waiting_For_UserName_To_Kick_in_Group1_AutoDrop_Settings, \
Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings, \
Waiting_For_UserName_To_Add_in_Group1_FollowAdmins_Settings, \
Waiting_For_UserName_To_Kick_in_Group1_FollowAdmins_Settings, \
Waiting_For_Status_To_Change_in_Group1_FollowAdmins_Settings = range(14)

Save_File_in_Group1_FollowAdmins_Settings = "C:/Users/44744/Documents/Project2/Group_1/Group1_Admins_IG.csv"
Colunm_Name_in_Group1_FollowAdmins_Setting = "UserNames"





#==================================================



reply_keyboard_in_Group1_FollowAdmins_Settings = [
    ['Add admin Instagram username', "Remove admin Instagram username"],
    ['See admin Instagram list', "Turn Off/On"],
    ['Done', "Home"],
]
markup_in_Group1_FollowAdmins_Settings = ReplyKeyboardMarkup(reply_keyboard_in_Group1_FollowAdmins_Settings, one_time_keyboard=True, resize_keyboard = True)


def start_in_Group1_FollowAdmins_Settings(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please navigate me by using the buttons below.😊",
        reply_markup=markup_in_Group1_FollowAdmins_Settings,
    )

    return Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings



#-Add username-----------------------------------------------------------------------

def Add_Admin_UserName_in_Group1_FollowAdmins_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Please, enter the @username of the user.')

    return Waiting_For_UserName_To_Add_in_Group1_FollowAdmins_Settings



def Add_Admin_Member_Task_Complete_Message_in_Group1_FollowAdmins_Settings(update: Update, context: CallbackContext) -> int:

    if "@" in update.message.text:
        with open(Save_File_in_Group1_FollowAdmins_Settings, 'a') as file:
            file.write("\n{}".format(update.message.text))

        update.message.reply_text(
            "{} has been added to your admin list.".format(update.message.text),
            reply_markup=markup_in_Group1_FollowAdmins_Settings,
        )

        return Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings

    else:
        update.message.reply_text(
            "Your username needs an @, Please try again.😅"
        )


        return Waiting_For_UserName_To_Add_in_Group1_FollowAdmins_Settings

#---------------------------------------------------------------




#-Kick username-----------------------------------------------------------------------

def Kick_Admin_UserName_in_Group1_FollowAdmins_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Please, enter the @username of the user.')

    return Waiting_For_UserName_To_Kick_in_Group1_FollowAdmins_Settings



def Kick_Admin_Member_Task_Complete_Message_in_Group1_FollowAdmins_Settings(update: Update, context: CallbackContext) -> int:
    if "@" in update.message.text:

        df = pd.read_csv(Save_File_in_Group1_FollowAdmins_Settings)
        UserNames_From_File = []

        for Loop_Over_UserName1 in df[Colunm_Name_in_Group1_FollowAdmins_Setting].dropna():
            UserNames_From_File.append(Loop_Over_UserName1)

        Filtered_Usernames = []

        for Loop_Over_UserNames2 in UserNames_From_File:
            if Loop_Over_UserNames2 != update.message.text:
                Filtered_Usernames.append(Loop_Over_UserNames2)
            else:
                pass

        with open(Save_File_in_Group1_FollowAdmins_Settings, "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow([Colunm_Name_in_Group1_FollowAdmins_Setting])

        with open(Save_File_in_Group1_FollowAdmins_Settings, "a+", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            for Loop_Over_UserNames3 in Filtered_Usernames:
                writer.writerow([Loop_Over_UserNames3])

        update.message.reply_text(
            "{} has been removed from your admin list.".format(update.message.text),
            reply_markup=markup_in_Group1_FollowAdmins_Settings,
        )

        return Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings

    else:
        update.message.reply_text(
            "Your username needs an @, Please try again.😅"
        )

        return Waiting_For_UserName_To_Kick_in_Group1_FollowAdmins_Settings


#---------------------------------------------------------------



#-Change_Follow_Admin_Status-----------------------------------------------------------------------

def Change_Follow_Admin_Status_in_Group1_FollowAdmins_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Would you like to turn this rule On or Off?')

    return Waiting_For_Status_To_Change_in_Group1_FollowAdmins_Settings



def Change_Follow_Admin_Status_Task_Complete_Message_in_Group1_FollowAdmins_Settings(update: Update, context: CallbackContext) -> int:

    if "Off" in update.message.text or "On" in update.message.text:

        if str(update.message.text).upper() == "OFF":
            df1 = pd.read_csv("C:/Users/44744/Documents/Project2/Group_1/Group1_Settings.csv")
            df1.at[0, "FollowAdmins_Status"] = "OFF"
            df1.to_csv("C:/Users/44744/Documents/Project2/Group_1/Group1_Settings.csv", index=False)

            update.message.reply_text(
                "Follow all admin rule has been turned OFF.".format(update.message.text),
                reply_markup=markup_in_Group1_FollowAdmins_Settings,
            )

            return Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings
        elif str(update.message.text).upper() == "ON":
            df1 = pd.read_csv("C:/Users/44744/Documents/Project2/Group_1/Group1_Settings.csv")
            df1.at[0, "FollowAdmins_Status"] = "ON"
            df1.to_csv("C:/Users/44744/Documents/Project2/Group_1/Group1_Settings.csv", index=False)

            update.message.reply_text(
                "Follow all admin rule has been turned ON.".format(update.message.text),
                reply_markup=markup_in_Group1_FollowAdmins_Settings,
            )

            return Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings

    else:
        update.message.reply_text(
            "Oops, Please enter 'Off' or 'On'."
        )


        return Waiting_For_Status_To_Change_in_Group1_FollowAdmins_Settings

#---------------------------------------------------------------


#--see list------------------------------------------------


def See_List_in_Group1_FollowAdmins_Settings(update: Update, context: CallbackContext) -> int:
    df = pd.read_csv(Save_File_in_Group1_FollowAdmins_Settings)

    update.message.reply_text(df.to_string(header = False, index = False), reply_markup=markup_in_Group1_FollowAdmins_Settings)

    return Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings



#----------------------------------------------------------
