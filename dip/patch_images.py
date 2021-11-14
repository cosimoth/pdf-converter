#!/usr/local/bin/python3
import cv2 as cv
import numpy as np
import os

script_path = os.path.abspath(os.path.dirname(__file__))
book_path = os.path.join(script_path, 'book')
save_path = os.path.join(script_path, 'refined')
image_names = [f for f in os.listdir(book_path) if os.path.isfile(os.path.join(book_path, f))]

win_size = (32, 32)
block_size = (16, 16)
block_stride = (8, 8)
cell_size = (8, 8)
nbins = 9
hog = cv.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)

template_path = os.path.join(script_path, 'patch')
line_template = cv.imread(os.path.join(template_path, 'line.jpg'), cv.IMREAD_GRAYSCALE)
note_templates = [cv.imread(os.path.join(template_path, '%d.jpg' % i), 0) for i in range(1, 5)]
line_feat = hog.compute(cv.resize(line_template, win_size))
note_feats = [hog.compute(cv.resize(note_template, win_size)) for note_template in note_templates] 

step = 1
thres = 1.2

def sliding_window(img, window_size, step, thres, template_feat):
    h, w = img.shape[:2]
    ph, pw = window_size[:2]
    min_loss = float('inf')
    for y in range(0, h - ph, step):
        for x in range(0, w - pw, step):
            patch = img[y:y+ph, x:x+pw]
            patch_feat = hog.compute(cv.resize(patch, win_size))
            loss = cv.norm(patch_feat, template_feat, cv.NORM_L2)
            if loss < min_loss: 
                min_loss = loss
                loc = (x, y)
    print(min_loss, loc)
    if min_loss < thres:
        return loc, (loc[0] + pw, loc[1] + ph)
    return None, None

for image_name in image_names:        
    # image_name = '021.jpg'
    image_idx, suffix = image_name.split('.', 1)
    print('page:', image_name)

    image_path = os.path.join(book_path, image_name)
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    bg_color = (255, )

    # page number
    cv.rectangle(img, (0, 0), (img.shape[1] ,100), bg_color, cv.FILLED)
    cv.imwrite(os.path.join(save_path, '1_no_page_number', image_name), img)

    # note line
    tl, br = sliding_window(img, line_template.shape, step, 2, line_feat)
    if tl is None:
        print('No line detect')
        continue
    cut = img[tl[1]:, :]
    cv.imwrite(os.path.join(save_path, 'cut', '%s_%s.%s' % (image_idx, 'line', suffix)), cut)
    cv.rectangle(img, (0, tl[1]), (img.shape[1], img.shape[0]), bg_color, cv.FILLED)
    cv.imwrite(os.path.join(save_path, '2_no_line', image_name), img)

    # note marks
    for idx, note_feat in enumerate(note_feats):
        note_template = note_templates[idx]
        tl, br = sliding_window(img, note_template.shape, step, 1.2, note_feat)
        if tl is None: 
            print('No [%d] detect' % (idx + 1))
            break
        cut = img[tl[1]:br[1], tl[0]:br[0]]
        cv.imwrite(os.path.join(save_path, 'cut', '%s_%d.%s' % (image_idx, idx + 1, suffix)), cut)
        cv.rectangle(img, tl, br, bg_color, cv.FILLED)
        cv.imwrite(os.path.join(save_path, '3_no_note_mark', '%s_no_%d.%s' % (image_idx, idx + 1, suffix)), img)
