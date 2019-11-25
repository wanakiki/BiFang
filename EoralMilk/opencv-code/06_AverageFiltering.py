#encoding:utf-8
from cv2 import cv2  
import numpy as np  
from matplotlib import pyplot as plt
 
#读取图片
img = cv2.imread('test.jpg')
#均值滤波
r = cv2.blur(img, (9,9))

#BGR2RGB
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
result = cv2.cvtColor(r,cv2.COLOR_BGR2RGB)
#显示图形
titles = ['Source Image', 'Blur Image']  
images = [source, result]  
for i in range(2):  
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  