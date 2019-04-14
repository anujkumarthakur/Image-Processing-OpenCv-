import cv2
import numpy as np
img = cv2.imread('Screenshot.jpg')

height,width=img.shape[:2]

roation_matrix= cv2.getRotationMatrix2D((width/2,height/2),180,.7)
rotate_image = cv2.warpAffine(img,roation_matrix,(width,height))

cv2.imshow('Rotated Image',rotate_image)
cv2.imshow('Orignal Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()