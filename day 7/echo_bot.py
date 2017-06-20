import telebot

token = "322921279:AAEOFAsRz9jg3mImCzjrZzB1vS7HWpzA-p4"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, это мы ботов тестим.")


@bot.message_handler(content_types=["text"])
def echo_all(message):
    text = message.text
    try:
        result = eval(text)
    except Exception as e:
        result= "Сорри чувак: "+str(e)
    bot.send_message(message.chat.id, result)


bot.polling(none_stop=True)
