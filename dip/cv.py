#!/usr/local/bin/python3
import cv2 as cv
import numpy as np
import os

script_path = os.path.abspath(os.path.dirname(__file__))

image_path = '%s/book/%03d.jpg' % (script_path, 7)
template_path = '%s/patch/%s.png' % (script_path, '1')

image = cv.imread(image_path)
color = tuple(map(int, image[0][0]))
print(type(color), color)
# color = (255, 255, 255)
tl, br = (49, 1343), (49 + 399, 1343 + 42)
cv.rectangle(image, tl, br, color, thickness=-1)
cv.imwrite(os.path.join(script_path, 'refined', 'a.jpg'), image)
