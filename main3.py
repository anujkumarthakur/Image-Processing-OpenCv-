import cv2
img = cv2.imread('Screenshot.jpg')
img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV_IMAGE',img_HSV)
cv2.imshow('HUE_CHANNEl',img_HSV[:,:,0])
cv2.imshow('Satutation',img_HSV[:,:,1])
cv2.imshow('Value',img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()