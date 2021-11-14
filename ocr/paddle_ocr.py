import os
import re
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

script_path = os.path.abspath(os.path.dirname(__file__))

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='ch', use_gpu=False) # need to run only once to download and load model into memory
img_path = os.path.join(script_path, 'book', '103.jpg')
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)
