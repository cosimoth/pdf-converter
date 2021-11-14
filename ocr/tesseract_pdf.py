import pdf2image
import pytesseract
from pytesseract import Output, TesseractError

pdf_path = '/mnt/c/Users/chepen/Downloads/44-真假袁世凯辨别.pdf'
# pdf_path = '/mnt/c/Users/chepen/Downloads/MS_eDeliveryConsent.pdf'

images = pdf2image.convert_from_path(pdf_path)

pil_im = images[5] # assuming that we're interested in the first page only

ocr_dict = pytesseract.image_to_data(pil_im, lang='chi_tra', output_type=Output.DICT)
# ocr_dict now holds all the OCR info including text and location on the image

text = ''.join(ocr_dict['text'])
print(text)