import cv2
img = cv2.imread('Screenshot.jpg')
roated_img = cv2.transpose(img)
cv2.imshow('Roated_image',roated_img)
cv2.imshow('origanel',img)
cv2.waitKey(0)
cv2.destroyAllWindows()