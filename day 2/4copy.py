from PIL import Image

im = Image.open('camel.jpg').convert('RGBA')  # открываем файл
pixels = im.load()  # получаем матрицу пикселей

width = im.width
height = im.height

im_small = im.copy()

size = (width // 2, height // 2)
im_small = im_small.resize(size)

im.paste(im_small, (0, 0, width // 2, height // 2))
im.paste(im_small, (width // 2, 0, 2 * (width // 2), height // 2))
im.paste(im_small, (0, height // 2, width // 2, 2 * (height // 2)))
im.paste(im_small, (width // 2, height // 2, 2 * (width // 2), 2 * (height // 2)))

im.show()
