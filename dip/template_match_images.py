#!/usr/local/bin/python3

import cv2 as cv
import numpy as np
import os

script_path = os.path.abspath(os.path.dirname(__file__))
book_path = os.path.join(script_path, 'book')
save_path = os.path.join(script_path, 'refined')
image_names = [f for f in os.listdir(book_path) if os.path.isfile(os.path.join(book_path, f))]

template_path = os.path.join(script_path, 'patch')
line_template = cv.imread(os.path.join(template_path, 'line.jpg'), cv.IMREAD_GRAYSCALE)
note_templates = [cv.imread(os.path.join(template_path, '%d.jpg' % i), 0) for i in range(1, 5)]
threshold = 0.8
method = cv.TM_CCOEFF_NORMED

def template_match(img_gray, template, method, threshold):
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        tl = min_loc
        score = 1 - min_val
    else:
        tl = max_loc
        score = max_val
    br = (tl[0] + w, tl[1] + h)
    print(score, tl)
    if score > threshold:
        return tl, br
    return None, None

for image_name in image_names:        
    # image_name = '047.jpg'
    image_idx, suffix = image_name.split('.', 1)
    print('page:', image_name)

    image_path = os.path.join(book_path, image_name)
    img = cv.imread(image_path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    bg_color = (255, 255, 255)

    # page number
    cv.rectangle(img, (0, 0), (img.shape[1] ,100), bg_color, cv.FILLED)
    cv.imwrite(os.path.join(save_path, '1_no_page_number', image_name), img)

    # note line
    tl, br = template_match(img_gray, line_template, method, threshold)
    if tl is None:
        print('No line detect')
        continue
    cut = img[tl[1]:, :]
    cv.imwrite(os.path.join(save_path, 'cut', '%s_%s.%s' % (image_idx, 'line', suffix)), cut)
    cv.rectangle(img, (0, tl[1]), (img.shape[1], img.shape[0]), bg_color, cv.FILLED)
    cv.imwrite(os.path.join(save_path, '2_no_line', image_name), img)

    # note marks
    for idx, note_template in enumerate(note_templates):
        tl, br = template_match(img_gray, note_template, method, threshold)
        if tl is None: 
            print('No [%d] detect' % (idx + 1))
            break
        cut = img[tl[1]:br[1], tl[0]:br[0]]
        cv.imwrite(os.path.join(save_path, 'cut', '%s_%d.%s' % (image_idx, idx + 1, suffix)), cut)
        cv.rectangle(img, tl, br, bg_color, cv.FILLED)
        cv.imwrite(os.path.join(save_path, '3_no_note_mark', '%s_no_%d.%s' % (image_idx, idx + 1, suffix)), img)
    
    cv.imwrite(os.path.join(save_path, 'final', image_name), img)
