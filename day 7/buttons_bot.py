import telebot
from telebot import types

token = "322921279:AAEOFAsRz9jg3mImCzjrZzB1vS7HWpzA-p4"

bot = telebot.TeleBot(token=token)

users = {}

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Собак", callback_data="dogs")
    callback_button1 = types.InlineKeyboardButton(text="Кошек", callback_data="cats")
    keyboard.add(callback_button)
    keyboard.add(callback_button1)
    bot.send_message(message.chat.id, "Што вы хотите?", reply_markup=keyboard)

def send_error(message):
    bot.send_message(message.chat.id, "Мы чет попутали((")

def send_quantity(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Одну", callback_data="one")
    callback_button1 = types.InlineKeyboardButton(text="Много", callback_data="many")
    keyboard.add(callback_button)
    keyboard.add(callback_button1)
    bot.send_message(message.chat.id, "Сколько вы этого хотите?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        id = call.message.chat.id
        if call.data == "cats":
            users[id] = "cats"
            send_quantity(call.message)
        if call.data == "dogs":
            users[id] = "dogs"
            send_quantity(call.message)
        if call.data == "one" or call.data == "many":
            if id not in users.keys():
                send_error(call.message)
            bot.send_message(id, "Вы хотите {0} {1}".format(call.data, users[id]))


bot.polling(none_stop=True)