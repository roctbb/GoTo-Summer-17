from PIL import Image

im = Image.open('camel.jpg').convert('RGBA') # открываем файл
pixels = im.load() # получаем матрицу пикселей

width = im.width
height = im.height

for i in range(width):
    for j in range(height):
        r, g, b, a = pixels[i, j]
        r = 255 - g
        g = 255 - r
        b = 255 - b
        pixels[i, j] = (r, g, b, a)

im.show()