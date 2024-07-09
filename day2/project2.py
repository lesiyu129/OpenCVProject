import cv2
import numpy as np


# 坐标平移
def translate(img, x, y):
    """
      坐标平移变换
    :param img: 原始图像数据
    :param x:平移的x坐标
    :param y:平移的y坐标
    :return:返回平移后的图像
    """
    h, w = img.shape[:2]
    m = np.float32([[1, 0, x], [0, 1, y]])
    dst = cv2.warpAffine(img, m, (w, h))
    return dst


# 旋转
def rotate(img, angle, center=None, scale=1.0):
    """
    旋转变换
      :param img: 原始图像数据
    :param angle: 旋转角度
    :param center: 旋转中心，如果为None则以原图中心为旋转中心
    :param scale: 缩放比例，默认为1
    :return: 返回旋转后的图像
    """
    h, w = img.shape[:2]
    if center is None:
        center = (w / 2, h / 2)

    m = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(img, m, (w, h))
    return rotated


if __name__ == "__main__":
    im = cv2.imread("../data/lena.jpg")
    cv2.imshow("origin", im)

    # 向下平移50像素
    im_translate = translate(im, 0, 50)
    cv2.imshow("translate1", im_translate)

    # 向左平移50像素，向下平移50像素
    im_translate = translate(im, -50, 50)
    cv2.imshow("translate2", im_translate)

    # 逆时针旋转45度
    im_rotate = rotate(im, 45)
    cv2.imshow("rotate1", im_rotate)

    # 逆时针旋转180度
    im_rotate = rotate(im, 180)
    cv2.imshow("rotate2", im_rotate)

    # 逆时针旋转20度，旋转中心为原图左上叫（0，0）
    im_rotate = rotate(im, 20, center=(0, 0))
    cv2.imshow("rotate3", im_rotate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
