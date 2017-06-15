import random
from PIL import Image, ImageFilter

im = Image.open('camel.jpg').convert('RGBA') # открываем файл
pixels = im.load() # получаем матрицу пикселей

width = im.width
height = im.height

for i in range(width):
    for j in range(height//2):
        r, g, b, a = pixels[i, j]
        av = (r + b + g) // 3
        if av<128:
            pixels[i, j] = (0, 0, 0, a)
        else:
            pixels[i, j] = (255, 255, 255, a)

im.show()