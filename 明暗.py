'''上面案例和下面代码都是使用四近邻方式计算'''
import cv2
import numpy as np

#一般来说对比度超30可以算亮度足够
def contrast(img0):
    img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)  # 彩色转为灰度图片
    m, n = img1.shape
    # 图片矩阵向外扩展一个像素
    img1_ext = cv2.copyMakeBorder(img1, 1, 1, 1, 1, cv2.BORDER_REPLICATE) / 1.0  # 除以1.0的目的是uint8转为float型，便于后续计算
    rows_ext, cols_ext = img1_ext.shape
    b = 0.0
    for i in range(1, rows_ext - 1):
        for j in range(1, cols_ext - 1):
            b += ((img1_ext[i, j] - img1_ext[i, j + 1]) ** 2 + (img1_ext[i, j] - img1_ext[i, j - 1]) ** 2 +
                  (img1_ext[i, j] - img1_ext[i + 1, j]) ** 2 + (img1_ext[i, j] - img1_ext[i - 1, j]) ** 2)

    cg = b / (4 * (m - 2) * (n - 2) + 3 * (2 * (m - 2) + 2 * (n - 2)) + 2 * 4)  # 对应上面48的计算公式
    print(cg)


#img0 = cv2.imread('./photo/luorun/img/2.jpg')
img0 = cv2.imread('./dark.jpg')

contrast(img0)

