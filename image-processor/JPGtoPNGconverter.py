import sys
import os
from PIL import Image

# * Grab first and second arguments
image_folder = f'{sys.argv[1]}/'
output_folder = f'{sys.argv[2]}/'

# * check if output_folder exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# * loop through image_folder
for filename in os.listdir(image_folder):
    # * open each file inside image_folder
    img = Image.open(f'{image_folder}{filename}')
    # * grabs the name without the extension
    img_name = os.path.splitext(filename)[0]
    # * save it in PNG format
    img.save(f'{output_folder}{img_name}.png', 'png')