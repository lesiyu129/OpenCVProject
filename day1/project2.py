# opencv 灰度图转换
import cv2

# flags=1 表示彩色图，flags=0 表示灰度图
img = cv2.imread("../data/lena.jpg", flags=1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.waitKey()
cv2.destroyAllWindows()
