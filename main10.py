import cv2
import numpy as np
img = cv2.imread('Screenshot.jpg')
h,w = img.shape[:2]

start_row,start_col=int(h*.25),int(w*.25)

end_row,end_col=int(h*.75),int(w*.75)

croped=img[start_row:end_row,start_col:end_col]

cv2.imshow('orignal',img)
cv2.waitKey(0)

cv2.imshow('coped',croped)
cv2.waitKey(0)

cv2.destroyAllWindows()