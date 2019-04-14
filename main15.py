import  cv2
import numpy as np
img = cv2.imread('Screenshot.jpg',0)

height,width=img.shape

sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow("orignal",img)
cv2.waitKey(0)

cv2.imshow("soble x",sobel_x)
cv2.waitKey(0)

sobel_or = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("sobel or",sobel_or)
cv2.waitKey(0)

cv2.imshow("soble y",sobel_y)
cv2.waitKey(0)

laplace = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("lapace",laplace)
cv2.waitKey(0)

canny = cv2.Canny(img,20,170)
cv2.imshow('Caany',canny)
cv2.waitKey(0)
