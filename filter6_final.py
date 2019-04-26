import numpy as np 
import cv2

img = cv2.imread('lung2.jpg',cv2.IMREAD_GRAYSCALE)
img_out = img.copy()
        
cv2.imwrite('lung3.jpg',img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
