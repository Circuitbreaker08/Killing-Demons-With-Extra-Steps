from PIL import Image
import math
import sys

def biased_midpoint(a, b, bias):
    return a * (1 - bias) + b * bias

def bias_bias(a):
    return math.sqrt(a)

def shader(position):
    x, y = position
    return (
        int(biased_midpoint(228, 143, bias_bias(y/im.size[1])) - x/20),
        int(biased_midpoint(237, 11, bias_bias(y/im.size[1])) - x/20),
        int(biased_midpoint(51, 1, bias_bias(y/im.size[1])) - x/20)
    )

im = Image.open(sys.argv[1]).convert("RGBA")

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixel = im.getpixel((x, y))
        if pixel[3] > 0:
            im.putpixel((x, y), shader((x, y)))

im.save(sys.argv[2])