import numpy as np
import cv2


# 图像随机裁剪
def random_crop(img, w, h):
    start_x = np.random.randint(0, img.shape[1] - w)  # 裁剪起始x像素
    start_y = np.random.randint(0, img.shape[0] - h)  # 裁剪起始y像素

    new_img = img[start_y : start_y + h, start_x : start_x + w]  # 执行裁剪

    return new_img


# 图像中心裁剪
def center_crop(img, w, h):
    start_x = int(img.shape[1] / 2) - int(w / 2)  # 裁剪起始x像素
    start_y = int(img.shape[0] / 2) - int(h / 2)  # 裁剪起始y像素

    new_img = img[start_y : start_y + h, start_x : start_x + w]  # 执行裁剪

    return new_img


im = cv2.imread("../data/banana_1.png", 1)

new_img = random_crop(im, 200, 200)  # 随机裁剪
new_img2 = center_crop(im, 200, 200)  # 中心裁剪

cv2.imshow("orig", im)
cv2.imshow("random_crop", new_img)
cv2.imshow("center_crop", new_img2)

cv2.waitKey()
cv2.destroyAllWindows()
