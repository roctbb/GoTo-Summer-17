from PIL import Image

im = Image.open('camel.jpg').convert('RGBA') # открываем файл
pixels = im.load() # получаем матрицу пикселей

width = im.width
height = im.height

for i in range(width):
    for j in range(height):
        r, g, b, a = pixels[i, j]
        av = (r+b+g)//3
        pixels[i, j] = (av, av, av, a)

im.show()