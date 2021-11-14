# Import libraries
from PIL import Image
import pytesseract

image_counter = 2

filelimit = image_counter - 1

filename = '/mnt/c/Users/chepen/Downloads/6JCgP.png'

# Recognize the text as string in image using pytesserct
text = pytesseract.image_to_string(Image.open(filename), lang = "chi_sim")

print(text)