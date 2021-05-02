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
Waiting_For_UserName_To_Kick_in_Group1_Premium_Settings = range(5)


Save_File_in_Group1_Premium_Settings = "Group_1/Group1_Premium.csv"
Colunm_Name_in_Group1_Premium_Setting = "UserNames"





#-----------------------------------------------------------------


reply_keyboard_in_Group1_Premium_Settings = [
    ['Add username', "Remove username"],
    ['See premium list'],
    ['Done', "Home"],
]
markup_in_Group1_Premium_Settings = ReplyKeyboardMarkup(reply_keyboard_in_Group1_Premium_Settings, one_time_keyboard=True, resize_keyboard = True)


def start_in_Group1_Premium_Settings(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please navigate me by using the buttons below.😊",
        reply_markup=markup_in_Group1_Premium_Settings,
    )

    return Waiting_For_User_Choice_in_Group1_Premium_Settings



#-Add username-----------------------------------------------------------------------

def Add_Premuim_UserName_in_Group1_Premium_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Please, enter the @username of the user.')

    return Waiting_For_UserName_To_Add_in_Group1_Premium_Settings



def Add_Premium_Member_Task_Complete_Message_in_Group1_Premium_Settings(update: Update, context: CallbackContext) -> int:

    if "@" in update.message.text:
        with open(Save_File_in_Group1_Premium_Settings, 'a') as file:
            file.write("\n{}".format(update.message.text))

        update.message.reply_text(
            "{} has been added to your premium list.".format(update.message.text),
            reply_markup=markup_in_Group1_Premium_Settings,
        )

        return Waiting_For_User_Choice_in_Group1_Premium_Settings

    else:
        update.message.reply_text(
            "Your username needs an @, Please try again.😅"
        )


        return Waiting_For_UserName_To_Add_in_Group1_Premium_Settings

#---------------------------------------------------------------




#-Kick username-----------------------------------------------------------------------

def Kick_Premuim_UserName_in_Group1_Premium_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Please, enter the @username of the user.')

    return Waiting_For_UserName_To_Kick_in_Group1_Premium_Settings



def Kick_Premium_Member_Task_Complete_Message_in_Group1_Premium_Settings(update: Update, context: CallbackContext) -> int:
    if "@" in update.message.text:

        df = pd.read_csv(Save_File_in_Group1_Premium_Settings)
        UserNames_From_File = []

        for Loop_Over_UserName1 in df[Colunm_Name_in_Group1_Premium_Setting].dropna():
            UserNames_From_File.append(Loop_Over_UserName1)

        Filtered_Usernames = []

        for Loop_Over_UserNames2 in UserNames_From_File:
            if Loop_Over_UserNames2 != update.message.text:
                Filtered_Usernames.append(Loop_Over_UserNames2)
            else:
                pass

        with open(Save_File_in_Group1_Premium_Settings, "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow([Colunm_Name_in_Group1_Premium_Setting])

        with open(Save_File_in_Group1_Premium_Settings, "a+", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            for Loop_Over_UserNames3 in Filtered_Usernames:
                writer.writerow([Loop_Over_UserNames3])

        update.message.reply_text(
            "{} has been removed from your premium list.".format(update.message.text),
            reply_markup=markup_in_Group1_Premium_Settings,
        )

        return Waiting_For_User_Choice_in_Group1_Premium_Settings

    else:
        update.message.reply_text(
            "Your username needs an @, Please try again.😅"
        )

        return Waiting_For_UserName_To_Kick_in_Group1_Premium_Settings


#---------------------------------------------------------------

#--see list------------------------------------------------


def See_List_in_Group1_Premium_Settings(update: Update, context: CallbackContext) -> int:
    df = pd.read_csv(Save_File_in_Group1_Premium_Settings)

    update.message.reply_text(df.to_string(header = False, index = False), reply_markup=markup_in_Group1_Premium_Settings)

    return Waiting_For_User_Choice_in_Group1_Premium_Settings



#----------------------------------------------------------

