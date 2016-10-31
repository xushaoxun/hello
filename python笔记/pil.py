# coding:utf-8
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random

im = Image.open('test.jpg')
w, h = im.size
im.thumbnail((w//2, h//2))
im.save('test2.jpg')

im = Image.open('test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('test_blur.jpg', 'jpeg')

def rndChr():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

w = 240
h = 60
image = Image.new('RGB', (w, h), (255, 255, 255))
font = ImageFont.truetype('arial.ttf')
draw = ImageDraw.Draw(image)
for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((60*t+10, 10), rndChr(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('test_captcha.jpg')