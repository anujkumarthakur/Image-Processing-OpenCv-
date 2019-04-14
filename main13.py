import cv2
import numpy as np
img = cv2.imread('Screenshot.jpg')
cv2.imshow("orignal",img)
cv2.waitKey(0)

kernal_3x3 = np.ones((3,3),np.float32)/9

blured = cv2.filter2D(img,-1,kernal_3x3)
cv2.imshow("3x3 kernal blured",blured)
cv2.waitKey(0)

kernal_7x7 = np.ones((7,7),np.float32)/49
blured2=cv2.filter2D(img,-1,kernal_7x7)
cv2.imshow("blured2",blured2)
cv2.waitKey(0)
cv2.destroyAllWindows()