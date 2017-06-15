import random
from PIL import Image

im = Image.open('camel.jpg').convert('RGBA') # открываем файл
pixels = im.load() # получаем матрицу пикселей

width = im.width
height = im.height

logo = Image.open('burzum.png').convert('RGBA') # открываем файл

for i in range(width):
    for j in range(height):
        r, g, b, a = pixels[i, j]
        av = (r + b + g) // 3
        if av<128:
            pixels[i, j] = (0, 0, 0, a)
        else:
            pixels[i, j] = (20, 20, 255, a)

box = (width//4, 0, 3*width//4, 2*height//10)

logo = logo.resize((2*width//4, 2*height//10))
im.paste(logo, box, logo)


im.show()