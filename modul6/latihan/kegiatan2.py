__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

from PIL import Image
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

background_path = os.path.join(current_dir, "img", "lucy.jpg")
overlay_path = os.path.join(current_dir, "img", "overlay.jpg")

background = Image.open(background_path)
overlay = Image.open(overlay_path)
overlay = overlay.convert("RGBA")
overlay = overlay.resize((100, 100))

x_position = 200
y_position = 200
background.paste(overlay, (x_position, y_position), overlay)

output_dir = os.path.join(current_dir, "img", "output")
output_path = os.path.join(output_dir, "output_kegiatan2.jpg")

os.makedirs(output_dir, exist_ok=True)

background.save(output_path)
background.show()
