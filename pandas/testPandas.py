import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR =1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE =0

##cv2.imshow('image',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

plt.imshow(img ,cmap='gray', interpolation ='bicubic')
plt.show()

