import cv2
import numpy as np

img = cv2.imread('Screenshot.jpg')
height,width = img.shape[:2]
print(height)
print(width)

quater_h,quater_w=height/2,width/16
print(quater_h)
print(quater_w)

T =np.float32([[1,0,quater_w],
             [0,1,quater_h]])
print(T)

img_trans=cv2.warpAffine(img,T,(height,width))
cv2.imshow("orignal",img)
cv2.imshow("Translation",img_trans)
cv2.waitKey(0)
cv2.destroyAllWindows()
