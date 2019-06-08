import random

from tg_bot import dispatcher
from random import choice
from telegram import Update, Bot
from telegram.ext import CommandHandler, Filters

bayramlar = ["Iyi bayramlar ", "Ooooooh iyi bayramlarrr "]

def mock(bot: Bot, update: Update):
	sentence = update.message.reply_to_message.text
	mockedText = ''.join(choice((str.upper, str.lower))(c) for c in sentence)
	bot.send_message(chat_id=update.message.chat_id, text=mockedText)

def bayram(bot: Bot, update: Update):
        try:
                sender_name = update.message.reply_to_message.from_user.first_name
        except:
                sender_name = update.message.from_user.first_name
        sender_name = sender_name + (sender_name[-1:]) * 3
        bot.send_message(chat_id=update.message.chat_id, text=bayramlar[random.randint(0,len(bayramlar)-1)] + sender_name)

MOCK_HANDLER = CommandHandler("mock", mock)
BAYRAM_HANDLER = CommandHandler("bayram", bayram)

dispatcher.add_handler(MOCK_HANDLER)
dispatcher.add_handler(BAYRAM_HANDLER)
