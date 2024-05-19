from PIL import Image
import os

def resize_image(image_path, output_path, size=(300, 300)):
    with Image.open(image_path) as img:
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)
