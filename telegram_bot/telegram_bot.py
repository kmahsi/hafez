from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.views.decorators.csrf import csrf_exempt
from telegram import ReplyKeyboardMarkup
import requests
import json
import random

updater = Updater('402599267:AAEQgkzMohV7bUj9QACnDYAC413AyoQLs8Q')
HAFEZ_FALL = 'نیت کن و فشار بده!'
HAFEZ_FALL_AGAIN = 'نیت مجدد!'


def user_information(update):
    user_id_get = update['message']['chat']['id']
    username_get = update['message']['chat']['username']
    first_name_get = update['message']['chat']['first_name']
    last_name_get = update['message']['chat']['last_name']
    requests.post('http://127.0.0.1:8000/setUserID/', json={"user_id": user_id_get, "username": username_get,
                                                            "first_name": first_name_get, "last_name": last_name_get})


@csrf_exempt
def random_set(data_length):
    numbers = random.sample(range(1, 10), len(str(data_length)))
    number = "".join(map(str, numbers))
    return number


def message_handler(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text
    if message == HAFEZ_FALL or HAFEZ_FALL_AGAIN:
        data_get = json.loads(requests.get('http://127.0.0.1:8000/hafezFall/').text)
        number = random_set(len(data_get))
        for data in data_get:
            data_id = data.get('id', '')
            if int(data_id) == int(number):
                data_text = data.get('text', '')
                data_description = data.get('description', '')
                data_list = "{0}\n\n{1}".format(data_text, data_description)
                keyboard = [[HAFEZ_FALL_AGAIN]]
                bot.send_message(chat_id, data_list, reply_markup=ReplyKeyboardMarkup(keyboard))
                break
    else:
        bot.send_message(chat_id, "عبارت وارد شده ناصحیح است، لطفا دکمه صحیح را انتخاب نمایید.")


def start(bot, update):
    chat_id = update.message.chat_id
    user_information(update)
    keyboard = [[HAFEZ_FALL]]
    bot.send_message(chat_id, "روز حافظ مبارک باد.", reply_markup=ReplyKeyboardMarkup(keyboard))


def main():
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler([Filters.text], message_handler))
    updater.start_polling()


if __name__ == '__main__':
    main()
