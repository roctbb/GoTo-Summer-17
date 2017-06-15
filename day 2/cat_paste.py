import random
from PIL import Image

im = Image.open('camel.jpg').convert('RGBA') # открываем файл
pixels = im.load() # получаем матрицу пикселей

cat_im = Image.open('cat.png').convert('RGBA') # открываем файл

width = im.width
height = im.height

for i in range(width):
    for j in range(height):
        r, g, b, a = pixels[i, j]
        av = (r+b+g)//3
        if random.randint(1,3)==1:
            pixels[i, j] = (0, random.randint(1,256), 0, a)
        else:
            pixels[i, j] = (255, 255, 255, a)

cat_im = cat_im.resize((width, height))
im.paste(cat_im, (0,0,width,height), cat_im)
im.show()