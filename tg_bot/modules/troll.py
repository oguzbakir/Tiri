import random

from tg_bot import dispatcher
from random import choice
from telegram import Update, Bot
from telegram.ext import CommandHandler, Filters

bayramlar = ["Iyi bayramlar ", "Ooooooh iyi bayramlarrr "]

def mock(bot: Bot, update: Update):
	message = update.effective_message
	if message.reply_to_message:
		sentence = update.message.reply_to_message.text
		mockedText = ''.join(choice((str.upper, str.lower))(c) for c in sentence)
		bot.send_message(chat_id=update.message.chat_id, text=mockedText)
	message.delete()

def bayram(bot: Bot, update: Update):
	chat_id = update.effective_chat.id
	message = update.effective_message
	if message.reply_to_message:
                sender_name = message.reply_to_message.from_user.first_name
	else:
                sender_name = message.from_user.first_name

	text = bayramlar[random.randint(0,len(bayramlar)-1)] + sender_name
	text = text + (text[-1:]) * 3

	if message.reply_to_message:
		reply_id = message.reply_to_message.message_id
		bot.send_message(chat_id, text, reply_to_message_id=reply_id)
	else:
		bot.send_message(chat_id, text)

	message.delete()

def gm(bot: Bot, update: Update):
	chat_id = update.effective_chat.id
	message = update.effective_message
	text = "GM yazılımla o özelliği kapattı"
	if message.reply_to_message:
		reply_id = message.reply_to_message.message_id
		bot.send_message(chat_id, text, reply_to_message_id=reply_id)
	else:
		bot.send_message(chat_id, text)
	message.delete()

MOCK_HANDLER = CommandHandler("mock", mock)
BAYRAM_HANDLER = CommandHandler("bayram", bayram)
GM_HANDLER = CommandHandler("gm", gm)

dispatcher.add_handler(MOCK_HANDLER)
dispatcher.add_handler(BAYRAM_HANDLER)
dispatcher.add_handler(GM_HANDLER)
