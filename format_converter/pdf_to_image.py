import pdf2image
import os

script_path = os.path.abspath(os.path.dirname(__file__))
pdf_path = '/mnt/c/Users/chepen/Downloads/44-真假袁世凯辨别.pdf'

images = pdf2image.convert_from_path(pdf_path)
for idx, image in enumerate(images):
    image.save('%s/book/%03d.jpg' % (script_path, idx), 'JPEG')
