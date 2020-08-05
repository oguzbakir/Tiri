import io
import json
import requests

from io import BytesIO
from tg_bot import dispatcher
from telegram import Update, Bot

from telegram.ext import CommandHandler


def getsticker(bot: Bot, update: Update):
    chat_id = update.effective_chat.id
    message = update.effective_message
    
    if not message.reply_to_message:
        bot.send_message(chat_id, "There is no message to get sticker from.")

    sticker = message.reply_to_message.sticker
    if sticker != None:
        f = bot.get_file(sticker.file_id)
        response = requests.get(f.file_path)
        image_bytes = io.BytesIO(response.content)
        bot.send_photo(chat_id, photo=image_bytes)


GETSTICKER_HANDLER = CommandHandler("getsticker", getsticker)

dispatcher.add_handler(GETSTICKER_HANDLER)
