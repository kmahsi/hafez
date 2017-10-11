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
    # print("we are in user information")
    user_id_get = update['message']['chat']['id']
    username_get = update['message']['chat']['username']
    first_name_get = update['message']['chat']['first_name']
    last_name_get = update['message']['chat']['last_name']
    requests.post('http://159.203.69.159:8000/setUserID/', json={"user_id": user_id_get, "username": username_get,
                                                                 "first_name": first_name_get,
                                                                 "last_name": last_name_get}, )


@csrf_exempt
def random_set(data_length):
    numbers = random.sample(range(1, 10), len(str(data_length)))
    number = "".join(map(str, numbers))
    return number


def message_handler(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text
    # print("i am at the top of message handler")
    # print (message)
    if message == HAFEZ_FALL or message == HAFEZ_FALL_AGAIN:
        data = json.loads(requests.get('http://159.203.69.159:8000/hafezFall/').text)

        # print("we are here")
        # print (data)
        # number = random.randint(1, (int(len(data_get))))
        # print ("len of data is", len(data_get))
        # print("number is ", number)
        # for data in data_get:
            # if int(data_id) == int(number):
        # data_id = data.get('id', '')
        data_text = data[0].get('text', '')
        # print (data_text)
        data_description = data[0].get('description', '')
        data_list = "{0}\n\n{1}".format(data_text, data_description)
        keyboard = [[HAFEZ_FALL_AGAIN]]
        # print ("before seing message")
        bot.send_message(chat_id, data_list, reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
        # print ("fall has sent")
        # print("the data's in data_get were invalid")
    else:
        # print ("incorrect term")
        bot.send_message(chat_id, "عبارت وارد شده ناصحیح است، لطفا دکمه صحیح را انتخاب نمایید.")
        bot.send_photo(chat_id=chat_id, photo=open('/home/kamran/Desktop/season/pic_for_season.jpg', 'rb'))

   # print()
   # print('\n')


def message_handler2(bot, update):
    pass


def start(bot, update):
    chat_id = update.message.chat_id
    user_information(update)
    # print("i am in start")
    keyboard = [[HAFEZ_FALL]]
    bot.send_message(chat_id, "روز حافظ مبارک باد.", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))


def main():
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler([Filters.text], message_handler))
    updater.dispatcher.add_handler(MessageHandler([Filters.text], message_handler2))

    updater.start_polling()


if __name__ == '__main__':
    main()
