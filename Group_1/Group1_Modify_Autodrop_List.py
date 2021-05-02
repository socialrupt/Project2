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

updater = Updater(token= pd.read_csv("Group_1/Group1_Global_Settings.csv")["Settings_Bot_Key"].iloc[0], use_context=True)


dispatcher = updater.dispatcher

#------------------------
UserName_Of_Owner = "Denny_Duque"#Denny_Duque wot_wanderer
Group_1_Username = pd.read_csv("Group_1/Group1_Global_Settings.csv")["Group_Username"].iloc[0]
#------------------------
Save_File_in_Group1_Premium_Settings = "Group_1/Group1_Premium.csv"
Save_File_in_Group1_GroupFormat_Settings = "Group_1/Group1_Settings.csv"
Save_File_in_Group1_AutoDrop_Settings = "Group_1/Group1_Autodrop.csv"
Colunm_Name_in_Group1_GroupFormat_Settings = "DxNum"
#------------------------------------------
Waiting_For_User_Choice, \
Waiting_For_Choice_Group1_Settings, \
Waiting_For_User_Choice_in_Group1_Premium_Settings, \
Waiting_For_UserName_To_Add_in_Group1_Premium_Settings, \
Waiting_For_UserName_To_Kick_in_Group1_Premium_Settings, \
Waiting_For_Number_in_Group1_GroupFormat_Settings, \
Waiting_For_User_Choice_in_Group1_AutoDrop_Settings, \
Waiting_For_UserName_To_Add_in_Group1_AutoDrop_Settings, \
Waiting_For_Limit_To_Add_in_Group1_AutoDrop_Settings, \
Waiting_For_UserName_To_Kick_in_Group1_AutoDrop_Settings = range(10)

#-Add username-----------------------------------------------------------------------

reply_keyboard_in_Group1_AutoDrop_Settings = [
    ['Add Instagram username', "Remove Instagram username"],
    ['See AutoDrop list'],
    ['Done', "Home"],
]
markup_in_Group1_AutoDrop_Settings = ReplyKeyboardMarkup(reply_keyboard_in_Group1_AutoDrop_Settings, one_time_keyboard=True, resize_keyboard = True)

def start_in_Group1_AutoDrop_Settings(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please navigate me by using the buttons below.😊",
        reply_markup=markup_in_Group1_AutoDrop_Settings,
    )

    return Waiting_For_User_Choice_in_Group1_AutoDrop_Settings


def Add_AutoDrop_UserName_in_Group1_AutoDrop_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Please, enter the Instagram @username of the user.')

    return Waiting_For_UserName_To_Add_in_Group1_AutoDrop_Settings

def Add_AutoDrop_Limit_in_Group1_AutoDrop_Settings(update: Update, context: CallbackContext) -> int:


    if "@" in update.message.text:
        with open(Save_File_in_Group1_AutoDrop_Settings, 'a') as file:
            file.write("\n{}".format(update.message.text))

        update.message.reply_text(
            "Please enter the daily limit for user.".format(update.message.text),
            reply_markup=markup_in_Group1_AutoDrop_Settings,
        )

        return Waiting_For_Limit_To_Add_in_Group1_AutoDrop_Settings

    else:
        update.message.reply_text(
            "Your Instagram username needs an @, Please try again.😅"
        )


        return Waiting_For_UserName_To_Add_in_Group1_AutoDrop_Settings

def Add_AutoDrop_Member_Task_Complete_Message_in_Group1_AutoDrop_Settings(update: Update, context: CallbackContext) -> int:
    try:
        if type(int(update.message.text)) == int:
            df11 = pd.read_csv(Save_File_in_Group1_AutoDrop_Settings)
            print(df11)
            df11.fillna(0, inplace=True)  # xhanges all the empty cells to 0
            #len(df11) - 1 means it adds it to the last row and don't create a new row (CURRENTLY WORKING)
            df11.loc[len(df11) - 1, "AutoDrop_Limit_Per_Day"] = update.message.text
            df11.to_csv(Save_File_in_Group1_AutoDrop_Settings, index=False)
            update.message.reply_text(
                "The username has been added to your AutoDrop list."
            )
            return Waiting_For_User_Choice_in_Group1_AutoDrop_Settings
        else:#This don't work but i have it just in case
            update.message.reply_text(
                "Please enter the daily limit for user, which needs to be a number."
            )
            return Waiting_For_Limit_To_Add_in_Group1_AutoDrop_Settings
    except ValueError:#If the input isn't a number then this will run.
        update.message.reply_text(
            "You need to send a number, Please try again.😅"
        )
        return Waiting_For_Limit_To_Add_in_Group1_AutoDrop_Settings
#---------------------------------------------------------------




#-Kick username-----------------------------------------------------------------------

def Kick_AutoDrop_UserName_in_Group1_AutoDrop_Settings(update: Update, context: CallbackContext) -> int:

    update.message.reply_text('Please, enter the Instagram @username of the user.')

    return Waiting_For_UserName_To_Kick_in_Group1_AutoDrop_Settings



def Kick_AutoDrop_Member_Task_Complete_Message_in_Group1_AutoDrop_Settings(update: Update, context: CallbackContext) -> int:
    if "@" in update.message.text:

        df = pd.read_csv(Save_File_in_Group1_AutoDrop_Settings)
        df = df[df.IG_Username != update.message.text]
        df.to_csv(Save_File_in_Group1_AutoDrop_Settings, index = False)#test this
        update.message.reply_text(
            "{} has been removed from your AutoDrop list.".format(update.message.text),
            reply_markup=markup_in_Group1_AutoDrop_Settings,
        )

        return Waiting_For_User_Choice_in_Group1_AutoDrop_Settings

    else:
        update.message.reply_text(
            "Your Instagram username needs an @, Please try again.😅"
        )

        return Waiting_For_UserName_To_Kick_in_Group1_AutoDrop_Settings


#---------------------------------------------------------------

#--see list------------------------------------------------


def See_List_in_Group1_AutoDrop_Settings(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Converting database into image..."
    )
    df = pd.read_csv(Save_File_in_Group1_AutoDrop_Settings)
    import dataframe_image as dfi
    dfi.export(df, 'Photo_Of_Autodrop_List.png')

    Bot_With_Token = telegram.Bot(token= pd.read_csv("Group_1/Group1_Global_Settings.csv")["Settings_Bot_Key"].iloc[0])

    Bot_With_Token.send_photo(chat_id = update.message.chat_id, photo = open("Photo_Of_Autodrop_List.png", "rb"))

    return Waiting_For_User_Choice_in_Group1_AutoDrop_Settings



#----------------------------------------------------------

