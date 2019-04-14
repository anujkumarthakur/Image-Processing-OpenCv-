import  cv2
import numpy as np
img = cv2.imread('Screenshot.jpg')
cv2.imshow('orignal',img)
cv2.waitKey(0)
M = np.ones(img.shape,dtype="uint8")*150
M1 = np.zeros(img.shape,dtype="uint8")+150
added = cv2.add(img,M1)
cv2.imshow('Added',added)

sub = cv2.subtract(img,M1)
cv2.imshow('Sub',sub)

mul = cv2.multiply(img,M1)
cv2.imshow('Mul',mul)

cv2.waitKey(0)
cv2.destroyAllWindows()
