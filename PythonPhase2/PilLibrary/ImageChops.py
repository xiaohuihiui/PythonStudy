from PIL import Image
im = Image.open('1.png')
from PIL import ImageChops
im_dup = ImageChops.duplicate(im)       # Duplicate the image, return a copy of the given image
print(im_dup.mode)                      # Output the mode
Mode: 'RGB'
im_diff = ImageChops.difference(im, im_dup)
                                        # Return an image formed by the absolute difference of the pixel values of the two images
im_diff.show()