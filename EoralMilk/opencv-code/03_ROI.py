# -*- coding:utf-8 -*-
from cv2 import cv2
import numpy as np

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

#显示原始图像
cv2.imshow("Demo", img)

#显示ROI区域
face = img[280:480, 430:730]
cv2.imshow("face", face)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()