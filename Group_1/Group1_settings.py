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


Save_File_in_Group1_Premium_Settings = "C:/Users/44744/Documents/Project2/Group_1/Group1_Premium.csv"
Colunm_Name_in_Group1_Premium_Settings = "UserNames"
#-----------------------------------------------------------------------
Save_File_in_Group1_GroupFormat_Settings = "C:/Users/44744/Documents/Project2/Group_1/Group1_Settings.csv"
Colunm_Name_in_Group1_GroupFormat_Settings = "DxNum"
df_in_Group1_GroupFormat_Settings = \
pd.read_csv(Save_File_in_Group1_GroupFormat_Settings)[Colunm_Name_in_Group1_GroupFormat_Settings].iloc[0]

reply_keyboard_in_Group1_Settings = [
    ['Premium Settings', "Change DX{}".format(df_in_Group1_GroupFormat_Settings)],
    ["AutoDrop Settings", "FollowAdmins Settings"],
    ["Warning System Settings"],
    ['Done', "Home"],
]
markup_in_Group1_Settings = ReplyKeyboardMarkup(reply_keyboard_in_Group1_Settings, one_time_keyboard=True, resize_keyboard = True)


def Group_1(update: Update, context: CallbackContext):

    df_in_Group1_GroupFormat_Settings = \
    pd.read_csv(Save_File_in_Group1_GroupFormat_Settings)[Colunm_Name_in_Group1_GroupFormat_Settings].iloc[0]
    reply_keyboard_in_Group1_Settings = [['Premium Settings', "Change DX{}".format(df_in_Group1_GroupFormat_Settings)],
                                         ["AutoDrop Settings", "FollowAdmins Settings"],
                                         ["Warning System Settings"],
                                         ['Done', "Home"], ]
    markup_in_Group1_Settings = ReplyKeyboardMarkup(reply_keyboard_in_Group1_Settings, one_time_keyboard=True,
                                                    resize_keyboard=True)

    update.message.reply_text(
        "Please tell me what you would like to do by using the buttons.😊",
        reply_markup=markup_in_Group1_Settings,
    )

    return Waiting_For_Choice_Group1_Settings