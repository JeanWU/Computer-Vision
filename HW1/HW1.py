# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:37:35 2018

@author: Jean
"""

import numpy as np
import cv2

img = cv2.imread('lena.bmp')

### 1. Upside Down 
upsidedown_img = img[::-1]

### 2. right-side-left
rightleft_img = img[::, ::-1]

### 3. diagonally mirrored 
mirror1=img
for i in range(mirror1.shape[0]):
    for j in range(mirror1.shape[1]):
        mirror1[i][j]=mirror1[j][i]
        
### 4. rotate lena.im 45 degrees clockwise
img = cv2.imread('lena.bmp')
image_center = tuple(np.array(img.shape[1::-1]) / 2)
rot_mat = cv2.getRotationMatrix2D(image_center, -45, 1.0)
rotate = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)


### 5 . shrink lena.im in half
half = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 

### 6. binarize lena.im at 128 to get a binary image
binary= cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]

### Output all images
cv2.imwrite('upsidedown_img.png', upsidedown_img)
cv2.imwrite('rightleft_img.png', rightleft_img)
cv2.imwrite('mirror1.png', mirror1)
cv2.imwrite('rotate.png', rotate)
cv2.imwrite('half.png', half)
cv2.imwrite('binary.png', binary)