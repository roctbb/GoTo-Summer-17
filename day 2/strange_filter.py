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

for i in range(width):
    for j in range(height//2, height):
        r, g, b, a = pixels[i, j]
        av = (r + b + g) // 3
        if av<128:
            pixels[i, j] = (0, 0, 0, a)
        else:
            pixels[i, j] = (20, 20, 255, a)

for i in range(width//2, width):
    for j in range(height):
        r, g, b, a = pixels[i, j]
        r = min(r+100,255)
        pixels[i ,j] = (r, g, b, a)

box = (width//6, height//6, 5*width//6, 5*height//6)
center_im = im.crop(box)
im = im.filter(ImageFilter.EMBOSS)
im.paste(center_im, box, center_im)



im.show()