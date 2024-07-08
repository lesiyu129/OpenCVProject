# 彩色亮度直方图均衡化
import cv2

original_img = cv2.imread("../data/sunrise.jpg")
cv2.imshow("original_img", original_img)

hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)

hsv_img[:, :, 2] = cv2.equalizeHist(hsv_img[:, :, 2])

original_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
cv2.imshow("equalizeHist", original_img)
cv2.waitKey()
cv2.destroyAllWindows()
