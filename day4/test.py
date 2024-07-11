import cv2
import matplotlib.pyplot as plt
import numpy as np


# 计算距离
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


img = cv2.imread("../data/paper.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_gauss = cv2.GaussianBlur(gray, (7, 7), 0)
gray_canny = cv2.Canny(gray_gauss, 30, 200)

contours, hierarchy = cv2.findContours(
    gray_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

# 计算面积
cuts = sorted(contours, key=cv2.contourArea, reverse=True)

docent = cuts[0]

# 获取顶点坐标
eps = 0.02 * cv2.arcLength(docent, True)
approx = cv2.approxPolyDP(docent, eps, True)
approx = approx.reshape(4, 2).astype(np.float32)
# for patch in approx:
# center = tuple(approx[3].astype(int))

# cv2.circle(img, center, 5, (0, 0, 255), 2)
#
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

left_up = approx[0]
left_down = approx[1]
right_down = approx[2]
right_up = approx[3]

print(left_up, left_down, right_down, right_up)

# 计算宽高
h = distance(left_up, left_down)
w = distance(left_up, right_up)

print(w, h)
# 输入图像四个顶点坐标
pts1 = np.float32(
    [
        left_up,
        left_down,
        right_down,
        right_up,
    ]
)
# 输出图像四个顶点坐标
pts2 = np.float32([[0, 0], [0, h], [w, h], [w, 0]])

# 透视变换
M = cv2.getPerspectiveTransform(pts1, pts2)
img_copy = img.copy()
img_warp = cv2.warpPerspective(img_copy, M, (int(w), int(h)))

# 输出结果
cv2.imshow("img", img_warp)
cv2.waitKey(0)
cv2.destroyAllWindows()
