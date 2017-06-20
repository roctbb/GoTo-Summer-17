import random
import telebot
import time
from threading import Thread

users = set()

token = "322921279:AAEOFAsRz9jg3mImCzjrZzB1vS7HWpzA-p4"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def about(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=rdg4lkgsQ04")

@bot.message_handler(commands=['spam'])
def start_spam(message):
    bot.send_message(message.chat.id, "Берем сироп вишневый!")
    users.add(message.chat.id)

@bot.message_handler(commands=['stop'])
def start_spam(message):
    bot.send_message(message.chat.id, "Ок, все")
    users.remove(message.chat.id)

def send_spam():
    while True:
        for user in users:
            bot.send_message(user, "Затем сироп вишневый!")
        time.sleep(2)

def make_polling():
    bot.polling(none_stop=True)

thread1 = Thread(target=send_spam)
thread2 = Thread(target=make_polling)

thread1.start()
thread2.start()








