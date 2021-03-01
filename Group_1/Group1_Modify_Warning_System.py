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
import telegram

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
Waiting_For_Status_To_Change_in_Group1_FollowAdmins_Settings, \
Waiting_For_User_Choice_in_Group1_WarningSystem_Settings, \
Waiting_For_Penalty_To_Change_in_Group1_WarningSystem_Settings, \
Waiting_For_NumberWarns_To_Change_in_Group1_WarningSystem_Settings, \
Waiting_For_Status_To_Change_in_Group1_WarningSystem_Settings = range(18)

Save_File_in_Group1_WarningSystem_Settings = "Group_1/Group1_Settings.csv"
Colunm_Name_in_Group1_WarningSystem_Setting1 = "Warning_Punishment"
Colunm_Name_in_Group1_WarningSystem_Setting2 = "NumWarns"
Colunm_Name_in_Group1_WarningSystem_Setting3 = "Warning_Status"



#==================================================



reply_keyboard_in_Group1_WarningSystem_Settings = [
    ['Change Punishment', "Change Number of warns"],
    ["Turn Off/On", "See Warning System Settings"],
    ['Done', "Home"],
]
markup_in_Group1_WarningSystem_Settings = ReplyKeyboardMarkup(reply_keyboard_in_Group1_WarningSystem_Settings, one_time_keyboard=True, resize_keyboard = True)


def start_in_Group1_WarningSystem_Settings(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please navigate me by using the buttons below.😊",
        reply_markup=markup_in_Group1_WarningSystem_Settings,
    )

    return Waiting_For_User_Choice_in_Group1_WarningSystem_Settings



#-Add username-----------------------------------------------------------------------

def Change_Penalty_in_Group1_WarningSystem_Settings(update: Update, context: CallbackContext) -> int:
    df1 = pd.read_csv("Group_1/Group1_Settings.csv").loc[0, "Warning_Status"]
    if df1.upper() == "ON":
        update.message.reply_text('1.Ban 2.Mute')
        update.message.reply_text('Please, enter the number of the new penalty.')

        return Waiting_For_Penalty_To_Change_in_Group1_WarningSystem_Settings
    else:
        update.message.reply_text("Your warning system is turned OFF, Please turn it ON then try again.")
        return Waiting_For_User_Choice_in_Group1_WarningSystem_Settings

def Change_Penalty_Task_Complete_Message_in_WarningSystem_Settings(update: Update, context: CallbackContext) -> int:
    try:
        if int(update.message.text) == 1 or int(update.message.text) == 2:
            Penaltys = {1: "Ban", 2: "Mute"}
            df1 = pd.read_csv("Group_1/Group1_Settings.csv")
            df1.loc[0, Colunm_Name_in_Group1_WarningSystem_Setting1] = str(Penaltys[int(update.message.text)])
            print(Penaltys[int(update.message.text)])
            df1.to_csv("Group_1/Group1_Settings.csv", index=False)

            update.message.reply_text(
                "Penalty for hitting the max warns has been changed to {}.".format(str(Penaltys[int(update.message.text)])),
                reply_markup=markup_in_Group1_WarningSystem_Settings,
            )

            return Waiting_For_User_Choice_in_Group1_WarningSystem_Settings
        else:
            update.message.reply_text(
                "Please enter a valid number, Please try again.😅"
            )


            return Waiting_For_Penalty_To_Change_in_Group1_WarningSystem_Settings

    except ValueError:
        update.message.reply_text(
            "You need to send a number, Please try again.😅"
        )

        return Waiting_For_Penalty_To_Change_in_Group1_WarningSystem_Settings

#---------------------------------------------------------------




#-Kick username-----------------------------------------------------------------------

def Change_Max_Warns_in_Group1_WarningSystem_Settings(update: Update, context: CallbackContext) -> int:
    df1 = pd.read_csv("Group_1/Group1_Settings.csv").loc[0, "Warning_Status"]
    if df1.upper() == "ON":
        update.message.reply_text('Please, enter the number of warns.')

        return Waiting_For_NumberWarns_To_Change_in_Group1_WarningSystem_Settings
    else:
        update.message.reply_text("Your warning system is turned OFF, Please turn it ON then try again.")
        return Waiting_For_User_Choice_in_Group1_WarningSystem_Settings


def Change_Max_Warns_Task_Complete_Message_in_Group1_WarningSystem_Settings(update: Update, context: CallbackContext) -> int:
    try:
        if type(int(update.message.text)) == type(int()):

            df1 = pd.read_csv("Group_1/Group1_Settings.csv")
            df1.at[0, Colunm_Name_in_Group1_WarningSystem_Setting2] = int(update.message.text)
            df1.to_csv("Group_1/Group1_Settings.csv", index=False)

            update.message.reply_text(
                "Number of max warns has been changed to {}.".format(update.message.text),
                reply_markup=markup_in_Group1_WarningSystem_Settings,
            )
            return Waiting_For_User_Choice_in_Group1_WarningSystem_Settings
        else:
            update.message.reply_text(
                "Your need to send a number, Please try again.😅"
            )

            return Waiting_For_NumberWarns_To_Change_in_Group1_WarningSystem_Settings

    except ValueError:
        update.message.reply_text(
            "You need to send a number, Please try again.😅"
        )
        return Waiting_For_NumberWarns_To_Change_in_Group1_WarningSystem_Settings



#---------------------------------------------------------------



#-Change_Follow_Admin_Status-----------------------------------------------------------------------

def Change_WarningSystem_Status_in_Group1_WarningSystem_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Would you like to turn this feature On or Off?')

    return Waiting_For_Status_To_Change_in_Group1_WarningSystem_Settings



def Change_WarningSystem_Status_Task_Complete_Message_in_Group1_WarningSystem_Settings(update: Update, context: CallbackContext) -> int:

    if "Off" in update.message.text or "On" in update.message.text:

        if str(update.message.text).upper() == "OFF":
            df1 = pd.read_csv("Group_1/Group1_Settings.csv")
            df1.loc[0, Colunm_Name_in_Group1_WarningSystem_Setting1] = "None"
            df1.loc[0, Colunm_Name_in_Group1_WarningSystem_Setting2] = "None"
            df1.at[0, Colunm_Name_in_Group1_WarningSystem_Setting3] = "OFF"
            df1.to_csv("Group_1/Group1_Settings.csv", index=False)

            update.message.reply_text(
                "Waring system has been turned OFF.".format(update.message.text),
                reply_markup=markup_in_Group1_WarningSystem_Settings,
            )

            return Waiting_For_User_Choice_in_Group1_WarningSystem_Settings
        elif str(update.message.text).upper() == "ON":
            df1 = pd.read_csv("Group_1/Group1_Settings.csv")
            df1.loc[0, Colunm_Name_in_Group1_WarningSystem_Setting1] = "Ban"#defualt
            df1.loc[0, Colunm_Name_in_Group1_WarningSystem_Setting2] = "3"#defualt
            df1.at[0, Colunm_Name_in_Group1_WarningSystem_Setting3] = "ON"
            df1.to_csv("Group_1/Group1_Settings.csv", index=False)

            update.message.reply_text(
                "Waring system has been turned ON.".format(update.message.text),
                reply_markup=markup_in_Group1_WarningSystem_Settings,
            )

            return Waiting_For_User_Choice_in_Group1_WarningSystem_Settings

    else:
        update.message.reply_text(
            "Oops, Please enter 'Off' or 'On'."
        )


        return Waiting_For_Status_To_Change_in_Group1_WarningSystem_Settings

#---------------------------------------------------------------

def See_Settings_in_Group1_WarningSystem_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Converting to image...')

    df = pd.read_csv("Group_1/Group1_Settings.csv")[["Warning_Status", "NumWarns", "Warning_Punishment"]]
    import dataframe_image as dfi
    dfi.export(df, 'Photo_Of_Warning_System.png')

    Bot_With_Token = telegram.Bot(token='1505711355:AAER5a9RirtlftUFmdkMjQ8F0towhw6Sp1g')

    Bot_With_Token.send_photo(chat_id = update.message.chat_id, photo = open("Photo_Of_Warning_System.png", "rb"))

    return Waiting_For_User_Choice_in_Group1_WarningSystem_Settings