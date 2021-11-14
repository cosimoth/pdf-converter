import cnocr
import os
import re

script_path = os.path.abspath(os.path.dirname(__file__))

book_path = os.path.join(script_path, 'refined', 'final')
image_names = [f for f in os.listdir(book_path) if os.path.isfile(os.path.join(book_path, f))]
ocr = cnocr.CnOcr()
# page_number_pattern = re.compile(r'^[0-9]{3}[^0-9]|[^0-9][0-9]{3}$')

with open(os.path.join(script_path, 'book_refined.txt'), 'a') as book:
    for image_name in image_names:        
        # image_name = '100.jpg'

        print('page:', image_name)
        image_path = os.path.join(book_path, image_name)
        res = ocr.ocr(image_path)

        # page = ''
        for idx, line in enumerate(res):
            words = ''.join(line[0]).strip()
            # if len(words) == 0:
            #     continue
            # elif words.startswith('[') or words.startswith('【'):
            #     print('skip comment:', words)
            #     break
            # elif page_number_pattern.search(words) and idx == 0:
            #     if image_name not in ['010.jpg', '011.jpg', '012.jpg']: 
            #         print('skip bookmark:', words)
            # else:
            book.write(words)
            # page += words
            if len(words) < 25:
                # page += '\n'
                book.write('\n')
        # print(page)
    
        if image_name == '50.jpg':
            break

