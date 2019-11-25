# -*- coding:utf-8 -*-
from cv2 import cv2 
import numpy as np
import random

#读取图片
img = cv2.imread("test.jpg")
#获取图像宽高
(h,w) = img.shape[:2]
#压缩原图尺寸并备份
img2 = cv2.resize(img, (int(w/3),int(h/3)), interpolation=cv2.INTER_CUBIC)

#随机生成噪点5000个
for t in range(5000): 
    i = random.randint(0,h - 1)
    j = random.randint(0,w - 1)
    color = (random.randrange(256),random.randrange(256),random.randrange(256))
    img[i,j] = color

#显示图像
cv2.namedWindow('Result', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow("Result", int(w/3),int(h/3))
cv2.imshow("Result", img)
cv2.imshow("Origin", img2)
#等待显示
#无限期等待输入
k=cv2.waitKey(0)
cv2.destroyAllWindows()

#写入图像
cv2.imwrite("testyxz.jpg", img)
