from PIL import Image, ImageFilter

img = Image.open("timg.jpg")
# img.show()

w, h = img.size

# img.thumbnail(w//2,h//2)
img.rotate(45)  # 旋转
# img.show()
# bands = img.getbands()
# print(bands)
# img = img.convert("L")
# img.show()

# img  = img.filter(ImageFilter.DETAIL) # 滤镜
# img.show()

p = img.histogram()  # 直方图
print(p)
# 加水印 其实就是两张图片进行合成
