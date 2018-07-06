# 
# Takes an image and splits it into 9 different slack
# emojis of appropriate dimensions
#

import Image
import os, sys

# open image
input_picture_name = sys.argv[1]
input_picture = Image.open(input_picture_name)
# resize to 384 x 384
new_size = (384, 384)
resized_image = input_picture.resize(new_size, Image.ANTIALIAS)

# create 9 images that are 128x128

resized_image.crop((0, 0, 50, 50)).save('output.png')

area_dictionary = {
    "top_left"       : (0,0,128,128),
    "top_middle"     : (128,0,256,128),
    "top_right"      : (256,0,384,128),

    "middle_left"   : (0,128,128,256),
    "middle_middle" : (128,128,256,256),
    "middle_right"  : (256,128,384,256),

    "bottom_left"   : (0,256,128,384),
    "bottom_middle" : (128,256,256,384),
    "bottom_right"  : (256,256,384,384)
}

picture_prefix = input_picture_name[0:-4]
for section in area_dictionary:
    resized_image.crop(area_dictionary[section]).save(picture_prefix + '_' + section + '.png')

# create tar of slack images
