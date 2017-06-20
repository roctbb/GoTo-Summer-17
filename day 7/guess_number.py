import random

import telebot

token = "322921279:AAEOFAsRz9jg3mImCzjrZzB1vS7HWpzA-p4"
bot = telebot.TeleBot(token)

data = {}


def init_user(id):
    if id not in data.keys():
        data[id] = {"number": 0, "wins": 0, "tries": 0}


def make_number(id):
    data[id]["number"] = random.randint(1, 20)
    data[id]["tries"] = 0
    bot.send_message(id, "Я загадал число, попробуй отгадать.")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    init_user(message.chat.id)
    make_number(message.chat.id)


@bot.message_handler(content_types=["text"])
def text_message(message):
    id = message.chat.id
    init_user(id)
    try:
        number = int(message.text)
    except:
        bot.send_message(id, "Это походу не число :(")
        return

    if number == data[id]["number"]:
        data[id]["wins"] += 1
        bot.send_message(id, "Ты отгадал за {tries} попыток! Отгадано {wins} чисел."
                         .format(tries=data[id]['tries'], wins=data[id]['wins']))
        make_number(id)
    else:
        data[id]["tries"] += 1
        bot.send_message(id, "Неверно! использовано {tries} попыток."
                         .format(tries=data[id]["tries"]))

bot.polling(none_stop=True)
