
# Pan picture #
import os
from pathlib import Path

path = r'C:\Users\Daniel\Desktop\OpenCVtest'
file = 'Pan_Pic.jpg'

path = Path(path)
os.chdir(path)
print(os.getcwd())

file_name = os.path.join(path, file)

import cv2
import numpy as np

img = cv2.imread(file_name)
scale = 135
w = int(img.shape[1]*scale/100)
h = int(img.shape[0]*scale/100)
dsize = (w, h)
img_resize = cv2.resize(img, dsize)

cv2.imshow("Image", img_resize)
cv2.waitKey(0)

cv2.imwrite('Pan_Pic_resized_35.jpg', img_resize)



# Baby Picture #

import os
from pathlib import Path

path = r'C:\Users\Daniel\Desktop\OpenCVtest'
file = 'TBBT4025.jpg'

path = Path(path)
os.chdir(path)
print(os.getcwd())

file_name = os.path.join(path, file)

import cv2
import numpy as np

img = cv2.imread(file_name)
# cv2.imshow("Image", img)
# cv2.waitKey(0)

h_scale = 28
w_scale = 25
w = int(img.shape[1]*h_scale/100)
h = int(img.shape[0]*w_scale/100)
dsize = (w, h)
img_resize = cv2.resize(img, dsize)

cv2.imshow("Image", img_resize)
cv2.waitKey(0)

cv2.imwrite('TBBT4025_resized_4x6.jpg', img_resize)
