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
Waiting_For_Number_in_Group1_GroupFormat_Settings = range(6)


Save_File_in_Group1_GroupFormat_Settings = "Group_1/Group1_Settings.csv"
Colunm_Name_in_Group1_GroupFormat_Settings = "DxNum"

#-----------------------------------------------------------------

reply_keyboard_in_Group1_GroupFormat_Settings = [
    ['Done', "Home"],
]
markup_in_Group1_GroupFormat_Settings = ReplyKeyboardMarkup(reply_keyboard_in_Group1_GroupFormat_Settings, one_time_keyboard=True, resize_keyboard = True)


def start_in_Group1_GroupFormat_Settings(update: Update, context: CallbackContext) -> int:
    df_in_Group1_GroupFormat_Settings = pd.read_csv(Save_File_in_Group1_GroupFormat_Settings)[Colunm_Name_in_Group1_GroupFormat_Settings].iloc[0]#Gets the value and it is used in the string bellow

    update.message.reply_text(
        "Please send a number for the new group format.😊".format(df_in_Group1_GroupFormat_Settings),
        reply_markup=markup_in_Group1_GroupFormat_Settings,
    )

    return Waiting_For_Number_in_Group1_GroupFormat_Settings

def Change_GroupFormat_Task_Complete_Message_in_Group1_GroupFormat_Settings(update: Update, context: CallbackContext) -> int:
    try:
        if type(int(update.message.text)) == int:
            if int(update.message.text) <= 100 and int(update.message.text) >= 3:
                df_in_Group1_GroupFormat_Settings = pd.read_csv(Save_File_in_Group1_GroupFormat_Settings)

                df_in_Group1_GroupFormat_Settings.loc[0,Colunm_Name_in_Group1_GroupFormat_Settings] = update.message.text
                df_in_Group1_GroupFormat_Settings.to_csv(Save_File_in_Group1_GroupFormat_Settings, index=False)

    #=========================================This section makes sure that the reply markup keybord has the write dxnum shown becuase it need to read the file again
                df_in_Group1_GroupFormat_Settings = pd.read_csv(Save_File_in_Group1_GroupFormat_Settings)[Colunm_Name_in_Group1_GroupFormat_Settings].iloc[0]
                reply_keyboard_in_Group1_Settings = [['Premium Settings', "Change DX{}".format(df_in_Group1_GroupFormat_Settings)],['Done', "Home"],]
                markup_in_Group1_Settings = ReplyKeyboardMarkup(reply_keyboard_in_Group1_Settings, one_time_keyboard=True, resize_keyboard = True)
                update.message.reply_text(
                    "Your group has been updated to a DX{}".format(update.message.text), reply_markup = markup_in_Group1_Settings
    #==============================================
                )
                return Waiting_For_Choice_Group1_Settings
            else:
                update.message.reply_text(
                    "Number MUST be between 3 and 100. Please try again."
                )
                return Waiting_For_Number_in_Group1_GroupFormat_Settings
        else:
            update.message.reply_text(
                "You need to send a number, Please try again.😅"
            )


            return Waiting_For_Number_in_Group1_GroupFormat_Settings
    except ValueError:
        update.message.reply_text(
            "You need to send a number, Please try again.😅"
        )
        return Waiting_For_Number_in_Group1_GroupFormat_Settings