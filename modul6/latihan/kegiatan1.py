__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

from PIL import Image, ImageOps, ImageDraw, ImageFont
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(current_dir, "img", "lucy.jpg")
img = Image.open(img_path)

font_path = os.path.join(current_dir, "font", "arial_bold.ttf")
custom_font = ImageFont.truetype(font_path, 24)

img_after = ImageOps.grayscale(img.copy())
draw = ImageDraw.Draw(img_after)

text = "Hi Muhammad Rizky Haksono, 202110370311325"
image_width, image_height = img.size

x_coordinate = 70
y_coordinate = 250

text_position = (x_coordinate, y_coordinate)
draw.text(text_position, text, font=custom_font, fill="black")

output_dir = os.path.join(current_dir, "img", "output")
output_path = os.path.join(output_dir, "output_kegiatan1.jpg")

img_after.save(output_path)
img_after.show()
