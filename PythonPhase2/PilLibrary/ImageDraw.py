from PIL import Image, ImageDraw

im = Image.open('1.png')

draw = ImageDraw.Draw(im)

draw.line((0,0)+im.size, fill=255)
draw.line((0, im.size[1], im.size[0], 0),fill=128)

im.show()