from PIL import Image

image = Image.open("images/5ae2e9db-bf5b-4f08-9b84-7ba4355a7b17.jpg")

box = (0, 0, image.width//2, image.height)
left_side = image.copy().crop(box)
left_side = left_side.transpose(Image.FLIP_LEFT_RIGHT)
left_side.show()
image.paste(left_side, (image.width//2, 0))
image.show()