import cv2
import numpy as np
img = cv2.imread('Screenshot.jpg')
cv2.imshow("orignal",img)
cv2.waitKey(0)

blur = cv2.blur(img,(3,3))
cv2.imshow("blur",blur)
cv2.waitKey(0)

gaussian =cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gausian",gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(img,5)
cv2.imshow("median",median)
cv2.waitKey(0)

bilatrial = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilatrial",bilatrial)
cv2.waitKey(0)
cv2.destroyAllWindows()