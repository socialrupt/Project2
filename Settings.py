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
#-----------
from Group_1.Group1_settings import *
from Group_1.Group1_Modify_Premium_List import *
from Group_1.Group1_Modify_Autodrop_List import *
from Group_1.Group1_Modify_Group_Format import *
from Group_1.Group1_Modify_FollowAdmin_List import *
from Group_1.Group1_Modify_Warning_System import *
#----------

updater = Updater(token= pd.read_csv("Group_1/Group1_Global_Settings.csv")["Settings_Bot_Key"].iloc[0], use_context=True)


dispatcher = updater.dispatcher

#------------------------
UserName_Of_Owner = "Denny_Duque"#Denny_Duque wot_wanderer
Group_1_Username = "featureamadx42"
#------------------------
Save_File_in_Group1_Premium_Settings = "Group_1/Group1_Premium.csv"
Save_File_in_Group1_GroupFormat_Settings = "Group_1/Group1_Settings.csv"
Save_File_in_Group1_AutoDrop_Settings = "Group_1/Group1_Autodrop.csv"
Save_File_in_Group1_FollowAdmins_Settings = "Group_1/Group1_Admins_IG.csv"
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
Waiting_For_UserName_To_Kick_in_Group1_AutoDrop_Settings, \
Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings, \
Waiting_For_UserName_To_Add_in_Group1_FollowAdmins_Settings, \
Waiting_For_UserName_To_Kick_in_Group1_FollowAdmins_Settings, \
Waiting_For_Status_To_Change_in_Group1_FollowAdmins_Settings, \
Waiting_For_User_Choice_in_Group1_WarningSystem_Settings, \
Waiting_For_Penalty_To_Change_in_Group1_WarningSystem_Settings, \
Waiting_For_NumberWarns_To_Change_in_Group1_WarningSystem_Settings, \
Waiting_For_Status_To_Change_in_Group1_WarningSystem_Settings = range(18)

reply_keyboard = [
    [Group_1_Username],
    ['Done'],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard = True)

#-----------------------------------------------------------------------

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Please navigate me by using the buttons below.😊",
        reply_markup=markup,
    )

    return Waiting_For_User_Choice

#--------------------------------------------------
def home(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Going home...",
        reply_markup=markup,
    )
    return Waiting_For_User_Choice

#-------------------------------------------------------------------------
def done(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(
        "BYE BYE!!"
    )

    return ConversationHandler.END
#-----------------------------------------------------------------



#========================================================

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start, Filters.user(username=UserName_Of_Owner) & Filters.chat_type.private)],#make this the username
    states={
        Waiting_For_User_Choice: [
            MessageHandler(
                Filters.regex('^({})$'.format(Group_1_Username)), Group_1
            ),

        ],
#===================================================================
        Waiting_For_Choice_Group1_Settings: [
            MessageHandler(
                Filters.regex('^(Premium Settings)$'), start_in_Group1_Premium_Settings
            ),
            MessageHandler(
                Filters.regex("Change"), start_in_Group1_GroupFormat_Settings
            ),
            MessageHandler(
                Filters.regex("^(AutoDrop Settings)$"), start_in_Group1_AutoDrop_Settings
            ),
            MessageHandler(
                Filters.regex("^(FollowAdmins Settings)$"), start_in_Group1_FollowAdmins_Settings
            ),
            MessageHandler(
                Filters.regex("^(Warning System Settings)$"), start_in_Group1_WarningSystem_Settings
            ),
        ],
#========================================================================
        Waiting_For_User_Choice_in_Group1_Premium_Settings: [
            MessageHandler(
                Filters.regex('^(Add username)$'), Add_Premuim_UserName_in_Group1_Premium_Settings
            ),
            MessageHandler(
                Filters.regex('^(Remove username)$'), Kick_Premuim_UserName_in_Group1_Premium_Settings
            ),
            MessageHandler(
                Filters.regex('^(See premium list)$'), See_List_in_Group1_Premium_Settings
            )

        ],

        Waiting_For_UserName_To_Add_in_Group1_Premium_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Add_Premium_Member_Task_Complete_Message_in_Group1_Premium_Settings,
            )

        ],

        Waiting_For_UserName_To_Kick_in_Group1_Premium_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Kick_Premium_Member_Task_Complete_Message_in_Group1_Premium_Settings,
            )

        ],
#=======================================================================================
        Waiting_For_Number_in_Group1_GroupFormat_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Change_GroupFormat_Task_Complete_Message_in_Group1_GroupFormat_Settings,
            )

        ],
#=======================================================================================
        Waiting_For_User_Choice_in_Group1_AutoDrop_Settings: [
            MessageHandler(
                Filters.regex('^(Add Instagram username)$'), Add_AutoDrop_UserName_in_Group1_AutoDrop_Settings
            ),
            MessageHandler(
                Filters.regex('^(Remove Instagram username)$'), Kick_AutoDrop_UserName_in_Group1_AutoDrop_Settings
            ),
            MessageHandler(
                Filters.regex('^(See AutoDrop list)$'), See_List_in_Group1_AutoDrop_Settings
            ),


        ],

        Waiting_For_UserName_To_Add_in_Group1_AutoDrop_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Add_AutoDrop_Limit_in_Group1_AutoDrop_Settings,
            )

        ],

        Waiting_For_Limit_To_Add_in_Group1_AutoDrop_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Add_AutoDrop_Member_Task_Complete_Message_in_Group1_AutoDrop_Settings,
            )

        ],

        Waiting_For_UserName_To_Kick_in_Group1_AutoDrop_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Kick_AutoDrop_Member_Task_Complete_Message_in_Group1_AutoDrop_Settings,
            )

        ],
#=======================================================================================
        Waiting_For_User_Choice_in_Group1_FollowAdmins_Settings: [
            MessageHandler(
                Filters.regex('^(Add admin Instagram username)$'), Add_Admin_UserName_in_Group1_FollowAdmins_Settings
            ),
            MessageHandler(
                Filters.regex('^(Remove admin Instagram username)$'), Kick_Admin_UserName_in_Group1_FollowAdmins_Settings
            ),
            MessageHandler(
                Filters.regex('^(See admin Instagram list)$'), See_List_in_Group1_FollowAdmins_Settings
            ),
            MessageHandler(
                Filters.regex('^(Turn Off/On)$'), Change_Follow_Admin_Status_in_Group1_FollowAdmins_Settings
            )

        ],

        Waiting_For_UserName_To_Add_in_Group1_FollowAdmins_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Add_Admin_Member_Task_Complete_Message_in_Group1_FollowAdmins_Settings,
            )

        ],

        Waiting_For_UserName_To_Kick_in_Group1_FollowAdmins_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Kick_Admin_Member_Task_Complete_Message_in_Group1_FollowAdmins_Settings,
            )

        ],
        Waiting_For_Status_To_Change_in_Group1_FollowAdmins_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Change_Follow_Admin_Status_Task_Complete_Message_in_Group1_FollowAdmins_Settings,
            )
        ],
#=======================================================================================
        Waiting_For_User_Choice_in_Group1_WarningSystem_Settings: [
            MessageHandler(
                Filters.regex('^(Change Punishment)$'), Change_Penalty_in_Group1_WarningSystem_Settings
            ),
            MessageHandler(
                Filters.regex('^(Change Number of warns)$'), Change_Max_Warns_in_Group1_WarningSystem_Settings
            ),
            MessageHandler(
                Filters.regex('^(Turn Off/On)$'), Change_WarningSystem_Status_in_Group1_WarningSystem_Settings
            ),
            MessageHandler(
                Filters.regex('^(See Warning System Settings)$'), See_Settings_in_Group1_WarningSystem_Settings
            )

        ],

        Waiting_For_Penalty_To_Change_in_Group1_WarningSystem_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Change_Penalty_Task_Complete_Message_in_WarningSystem_Settings,
            )

        ],

        Waiting_For_NumberWarns_To_Change_in_Group1_WarningSystem_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Change_Max_Warns_Task_Complete_Message_in_Group1_WarningSystem_Settings,
            )

        ],
        Waiting_For_Status_To_Change_in_Group1_WarningSystem_Settings: [
            MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex('^Done$') | Filters.regex('^Home$')),
                Change_WarningSystem_Status_Task_Complete_Message_in_Group1_WarningSystem_Settings,
            )

        ],

    },
    fallbacks=[MessageHandler(Filters.regex('^Done$'), done),
               MessageHandler(Filters.regex('^Home$'), home)],
    conversation_timeout = 1000
)

dispatcher.add_handler(conv_handler)


updater.start_polling()

updater.idle()

