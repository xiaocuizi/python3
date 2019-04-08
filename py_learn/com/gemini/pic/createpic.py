from PIL import Image, ImageDraw, ImageFont
import random as random


# 生成随机的字母
def rndChar():
    return chr(random.randint(65, 90))


# print(rndChar())
# 随机颜色
def rndColor1():
    return (random.randint(64, 256), random.randint(64, 256), random.randint(64, 256))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


#
w = 240
h = 60
# 画板
img = Image.new("RGB", (w, h), (255, 255, 255))

# 创建字体对象
font = ImageFont.truetype("arial.ttf", 36)

draw = ImageDraw.Draw(img)

for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=rndColor1())

for i in range(4):
    draw.text(((60 * i + 10), 10), rndChar(), font=font, fill=rndColor2())

#img.show()
img.save("aa", "jepg")
