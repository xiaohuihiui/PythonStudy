from PIL import Image

im = Image.open("1.png")

box = (100, 100, 400, 400)

region = im.crop(box)

region = region.transpose(Image.ROTATE_180)  # Counter-clockwise rotate 180

im.paste(region, box)