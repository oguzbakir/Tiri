from tg_bot import dispatcher
from telegram import Update, Bot

from requests import get
from telegram.ext import CommandHandler

def dolar(bot: Bot, update: Update):
    chat_id = update.effective_chat.id
    message = update.effective_message

    message_text = message.text
    message_split = message_text.split(" ")

    request_url = "https://api.exchangeratesapi.io/latest?base=USD"
    current_response = get(request_url).json()
    current_rate = float(current_response["rates"]["TRY"])
    amount = 1
    if len(message_split) == 2:
        try:
            amount = int(message_split[1])
        except ValueError:
            try:
                amount = float(message_split[1].replace(',','.'))
            except:
                pass
        if message.reply_to_message:
            reply_id = message.reply_to_message.message_id
            bot.send_message(chat_id, "{} Dolar = {} Türk Lirası".format(amount, current_rate * amount), reply_to_message_id=reply_id)
        else:
            bot.send_message(chat_id, "{} Dolar = {} Türk Lirası".format(amount, current_rate * amount))
    message.delete()

def euro(bot: Bot, update: Update):
    chat_id = update.effective_chat.id
    message = update.effective_message

    message_text = message.text
    message_split = message_text.split(" ")

    request_url = "https://api.exchangeratesapi.io/latest?base=EUR"
    current_response = get(request_url).json()
    current_rate = float(current_response["rates"]["TRY"])
    amount = 1
    if len(message_split) == 2:
        try:
            amount = int(message_split[1])
        except ValueError:
            try:
                amount = float(message_split[1].replace(',','.'))
            except:
                pass
        if message.reply_to_message:
            reply_id = message.reply_to_message.message_id
            bot.send_message(chat_id, "{} Euro = {} Türk Lirası".format(amount, current_rate * amount), reply_to_message_id=reply_id)
        else:
            bot.send_message(chat_id, "{} Euro = {} Türk Lirası".format(amount, current_rate * amount))
    message.delete()


DOLAR_HANDLER = CommandHandler("dolar", dolar)
EURO_HANDLER = CommandHandler("euro", euro)

dispatcher.add_handler(DOLAR_HANDLER)
dispatcher.add_handler(EURO_HANDLER)