import cv2

background = cv2.imread('lung3.jpg')
overlay = cv2.imread('lung4.jpg')

added_image = cv2.addWeighted(background,0.5,overlay,0.5,0)

cv2.imwrite('si.jpg', added_image)
cv2.imshow('image',added_image)
cv2.waitKey(0)
cv2.destroyAllWindows()