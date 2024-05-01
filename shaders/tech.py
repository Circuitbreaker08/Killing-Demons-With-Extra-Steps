from PIL import Image, ImageDraw
import sys

imd = ImageDraw.ImageDraw(Image.new())
print(imd.textbbox((0, 0), sys.argv[1]))