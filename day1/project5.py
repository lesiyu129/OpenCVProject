# 二值化与反二值化
import cv2

img = cv2.imread("../data/lena.jpg", 0)
cv2.imshow("img", img)

# 二值化
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret_inv, thresh_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("thresh", thresh)
cv2.imshow("thresh_inv", thresh_inv)
cv2.waitKey()
cv2.destroyAllWindows()
