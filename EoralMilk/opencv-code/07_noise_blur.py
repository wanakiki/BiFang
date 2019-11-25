#encoding:utf-8
from cv2 import cv2  
import numpy as np  
from matplotlib import pyplot as plt
import random
import copy
 
#读取图片
img = cv2.imread('test2.jpg')
#获取图像宽高
(h,w) = img.shape[:2]

#随机生成噪点5000个
n = copy.copy(img) 
#注意，这里进行了浅拷贝，备份了一份img用于noise，直接赋值会变成引用img
for t in range(5000): 
    i = random.randint(0,h - 1)
    j = random.randint(0,w - 1)
    color = (random.randrange(256),random.randrange(256),random.randrange(256))
    n[i,j] = color

#均值滤波
r = cv2.blur(n, (5,5))
#cv2.imshow("o",img)
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
noise = cv2.cvtColor(n,cv2.COLOR_BGR2RGB)
result = cv2.cvtColor(r,cv2.COLOR_BGR2RGB)

#显示图形
titles = ['Source Image', 'Noise Image', 'Blur Image']  
images = [source, noise, result]  
for i in range(3):  
   plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  