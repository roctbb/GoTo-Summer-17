import random

import telebot

token = "322921279:AAEOFAsRz9jg3mImCzjrZzB1vS7HWpzA-p4"
bot = telebot.TeleBot(token)

numbers = {}

def make_number(id):
    numbers[id] = random.randint(1, 20)
    bot.send_message(id, "Я загадал число, попробуй отгадать.")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    make_number(message.chat.id)

@bot.message_handler(content_types=["text"])
def text_message(message):
    id = message.chat.id
    if id in numbers.keys():
        if int(message.text) == numbers[id]:
            bot.send_message(id, "Ты угадал!")
            make_number(id)
        else:
            bot.send_message(id, "Неверно азаз!")
    else:
        make_number(id)



bot.polling(none_stop=True)