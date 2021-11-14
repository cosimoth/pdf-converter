from cnocr import CnOcr

image_path = '/mnt/c/Users/chepen/Downloads/6JCgP.png'

ocr = CnOcr()
res = ocr.ocr(image_path)
for line in res:
    print("Predicted Chars:", ''.join(line[0]))
