#encoding:utf-8
from cv2 import cv2  
import numpy as np  
from matplotlib import pyplot as plt
import random
import copy
 
#读取图片
img1 = cv2.imread('skly1.jpg')
img2 = cv2.imread('skly2.jpg')

result1 = cv2.add(img1,img2)
result2 = cv2.addWeighted(img1,0.5,img2,0.5,-5)
cv2.imwrite("skly_mix.jpg", result2)

o1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
o2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

r1 = cv2.cvtColor(result1,cv2.COLOR_BGR2RGB)
r2 = cv2.cvtColor(result2,cv2.COLOR_BGR2RGB)



#显示图形
titles = ['Source Image1', 'Source Image2', 'Add Image', 'Mix Image']  
images = [o1, o2, r1, r2]  
for i in range(4):  
   plt.subplot(1,4,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  