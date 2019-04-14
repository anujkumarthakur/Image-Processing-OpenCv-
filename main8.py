import cv2
import numpy as np
img = cv2.imread('Screenshot.jpg')

cv2.imshow('orignal',img)
cv2.waitKey(0)

img_scaled=cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow('scaled_image',img_scaled)
cv2.waitKey(0)

img_scaled1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Polation_IMAge',img_scaled1)
cv2.waitKey(0)

img_scaled2=cv2.resize(img,(900,700),interpolation=cv2.INTER_AREA)
cv2.imshow('Scalled_imahe2',img_scaled2)
cv2.waitKey(0)
cv2.destroyAllWindows()