import uuid
import telebot
from PIL import Image

token = "322921279:AAEOFAsRz9jg3mImCzjrZzB1vS7HWpzA-p4"
bot = telebot.TeleBot(token)

def process(filename):
    image = Image.open(filename)
    box = (0, 0, image.width // 2, image.height)
    left_side = image.copy().crop(box)
    left_side = left_side.transpose(Image.FLIP_LEFT_RIGHT)
    image.paste(left_side, (image.width // 2, 0))
    image.save(filename)

@bot.message_handler(content_types=["photo"])
def save(message):
    #скачивание файла
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)

    #узнаешь расширение и придумываем имя
    extn = '.' + str(path.file_path).split('.')[-1]
    cname = str(uuid.uuid4()) + extn

    #создаем файл и записываем туда данные
    with open('images/' + cname, 'wb') as new_file:
        new_file.write(downloaded_file)

    #применяем фильтр
    process('images/' + cname)

    #открываем файл и отправляем его пользователю
    with open('images/' + cname, 'rb') as new_file:
        bot.send_photo(message.chat.id, new_file.read())


bot.polling(none_stop=True)
