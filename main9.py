import cv2
img = cv2.imread('Screenshot.jpg')
smaller = cv2.pyrDown(img)
larger = cv2.pyrUp(img)
cv2.imshow('orignal',img)
cv2.imshow('smaller',smaller)
cv2.imshow('larger',larger)
cv2.waitKey(0)
cv2.destroyAllWindows()