import cv2
import numpy

img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('logo.jpg')
rows,cols,chnls = img2.shape

img = cv2.addWeighted(img1,0.7 ,img2 , 0.3 ,3)

roi = img1[0:rows , 0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2gray, 127,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

