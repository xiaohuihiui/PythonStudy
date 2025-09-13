from PIL import Image, ImageEnhance

im = Image.open('1.png')

draw = ImageEnhance.Brightness(im)
im0=draw.enhance(1.2)
im0.show()