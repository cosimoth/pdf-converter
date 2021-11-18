#!/usr/local/bin/python3

import cv2 as cv
import numpy as np
import os

script_path = os.path.abspath(os.path.dirname(__file__))
book_path = os.path.join(script_path, 'book')
patch_path = os.path.join(script_path, 'patch')

image_path = os.path.join(book_path, '038.jpg')
img = cv.imread(image_path)
patch = img[157:175, 252:273]
cv.imwrite(os.path.join(patch_path, '1.jpg'), patch)

image_path = os.path.join(book_path, '098.jpg')
img = cv.imread(image_path)
patch = img[683:701, 297:317]
cv.imwrite(os.path.join(patch_path, '2.jpg'), patch)
patch = img[836:854, 574:594]
cv.imwrite(os.path.join(patch_path, '3.jpg'), patch)
patch = img[1142:1160, 514:535]
cv.imwrite(os.path.join(patch_path, '4.jpg'), patch)

image_path = os.path.join(book_path, '064.jpg')
img = cv.imread(image_path)
patch = img[1291:1343, 116:371]
cv.imwrite(os.path.join(patch_path, 'line.jpg'), patch)