#!/usr/local/bin/python3

import cv2 as cv
import numpy as np
import os

script_path = os.path.abspath(os.path.dirname(__file__))

image_path = '%s/book/%03d.jpg' % (script_path, 7)
template_path = '%s/patch/%s.png' % (script_path, '1')

img_rgb = cv.imread(image_path)
img = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
# _, img = cv.threshold(img, 0, 1, cv.THRESH_OTSU)
# img = 1 - img
# img = cv.imread(image_path, 0)
template = cv.imread(template_path, 0)
# _, template = cv.threshold(template, 0, 1, cv.THRESH_OTSU)
# template = 1 - template
# template = img[1136:1136+24, 840:840+24]
# cv.imwrite(os.path.join(script_path, 'patch', '[1]_tmp.png'), template*255)

win_size = (32, 32)
block_size = (16, 16)
block_stride = (8, 8)
cell_size = (8, 8)
nbins = 9
hog = cv.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)
template_feat = hog.compute(cv.resize(template, win_size))

thres = 10
h = img.shape[0]
w = img.shape[1]
ph = template.shape[0]
pw = template.shape[1]
step = 1
# color = tuple(map(int, img[0][0]))
min = float('inf')
loc = None

for r in range(0, h - ph, step):
    for c in range(0, w - pw, step):
        patch = img[r:r+ph, c:c+pw]
        # loss = np.linalg.norm(patch - template)
        # if r == 1009 and c == 195:
        #     print(loss)
        #     save_path = os.path.join(script_path, 'res', 'temp.png')
        #     cv.imwrite(save_path, patch * 255)
        patch_feat = hog.compute(cv.resize(patch, win_size))
        loss = cv.norm(patch_feat, template_feat, cv.NORM_L2)
        if loss < min: 
            min = loss
            loc = (c, r)
            # cv.rectangle(img_rgb, loc, (loc[0] + pw, loc[1] + ph), (0, 0, 255), thickness=10)
            # print(loc, loss)

cv.rectangle(img_rgb, loc, (loc[0] + pw, loc[1] + ph), (0, 0, 255), thickness=10)
print(min)
print(loc)
cv.imwrite(os.path.join(script_path, 'res', 'res.jpg'), img_rgb)

# Load the aerial image and convert to HSV colourspace
# image = cv2.imread(image_path)
# color = tuple(map(int, image[0][0]))
# print(type(color), color)
# # color = (255, 255, 255)
# p1 = (100, 100)
# p2 = (1000, 1000)
# cv2.rectangle(image, p1, p2, color, thickness=-1)
# cv2.imwrite('a.jpg', image)
