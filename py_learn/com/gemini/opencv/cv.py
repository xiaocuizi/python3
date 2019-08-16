import cv2

img = cv2.imread("mei.png")
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 主题

## 划线
green = (0,255,0)
# cv2.line(img,(0,0),(300,300),green,3)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ❀ 画圆
# cv2.circle(img,(150,150),100,green,2)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 矩形
cv2.rectangle(img,(170,110),(320,260),green,2)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()