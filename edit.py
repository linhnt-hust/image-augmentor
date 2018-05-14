import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('0001001.jpg')
#cv2.imshow('image',img)
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.show()
height, width = img.shape[:2]

#dst = cv2.pyrUp(img, (height*1.2, width*1.2))

res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_AREA)
dst = res[10:224, 10:224] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
cv2.imshow("cropped", dst)


k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('0001001_edit.jpg',dst)
    cv2.destroyAllWindows()