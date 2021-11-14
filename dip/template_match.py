#!/usr/local/bin/python3
import cv2 as cv
import numpy as np
import os

script_path = os.path.abspath(os.path.dirname(__file__))
image_path = '%s/book/%03d.jpg' % (script_path, 16)
template_path = '%s/patch/%s.jpg' % (script_path, '1')

img_rgb_src = cv.imread(image_path)
img_gray_src = cv.cvtColor(img_rgb_src, cv.COLOR_BGR2GRAY)
template = cv.imread(template_path, 0)
w, h = template.shape[::-1]
# res = cv.matchTemplate(img_gray,template, cv.TM_CCOEFF_NORMED)
# threshold = 0.5
# loc = np.where(res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
# cv.imwrite('res.png',img_rgb)

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img_rgb = img_rgb_src.copy()
    img_gray = img_gray_src.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img_gray,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img_rgb,top_left, bottom_right, (0, 0, 255), 3)
    cv.imwrite(os.path.join(script_path, 'test', meth + '.jpg'), img_rgb)

# Load the aerial image and convert to HSV colourspace
# image = cv2.imread(image_path)
# color = tuple(map(int, image[0][0]))
# print(type(color), color)
# # color = (255, 255, 255)
# p1 = (100, 100)
# p2 = (1000, 1000)
# cv2.rectangle(image, p1, p2, color, thickness=-1)
# cv2.imwrite('a.jpg', image)
