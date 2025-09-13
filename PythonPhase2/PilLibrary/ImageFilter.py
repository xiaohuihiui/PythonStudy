from PIL import Image
im = Image.open('1.png')

from PIL import ImageFilter

imout = im.filter(ImageFilter.BLUR)

print(imout.size)
imout.show()