# opencv读写图像
import cv2

img = cv2.imread("../data/lena.jpg")
cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("./lena.jpg", img)
