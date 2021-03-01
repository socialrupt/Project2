import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import telegram.error
import csv
import pandas as pd
import sys

Bot_With_Token = telegram.Bot(token='1556820797:AAH172KNLitYDHfdyPMLanWyJnK5xuGrVx8')

Bot_With_Token.kick_chat_member("-1001481095105", 1393680824)


