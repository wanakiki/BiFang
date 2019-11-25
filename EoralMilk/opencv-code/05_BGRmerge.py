from cv2 import cv2
import numpy as np

#读取图片
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)

#拆分通道
b, g, r = cv2.split(img)

#合并通道
m = cv2.merge([b, g, r])
cv2.imshow("Merge", m)

#拆分通道
rows, cols, chn = img.shape
z = np.zeros((rows,cols),dtype=img.dtype)
b = cv2.split(img)[0]
g = cv2.split(img)[1]
r = cv2.split(img)[2]

cv2.imshow("Zero",z)

#合并通道（只留Blue通道）
m = cv2.merge([b, z, z])
cv2.imshow("BlueOnly", m)
#green
m = cv2.merge([z, g, z])
cv2.imshow("GreenOnly", m)
#red
m = cv2.merge([z, z, r])
cv2.imshow("RedOnly", m)


           
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
