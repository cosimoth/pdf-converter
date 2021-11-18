#!/usr/local/bin/python3

import argparse
import pdf2image
import os

def windows_path_to_wsl_path(path):
    if ':' not in path:
        return path
    path = path.replace('\\', '/')
    d, p = path.split(':', 1)
    return '/mnt/%s/%s' % (d.lower(), p.strip('/'))

def convert_pdf_to_image(pdf_path, image_path):
    pdf_path = windows_path_to_wsl_path(pdf_path)
    print("PDF path:", pdf_path)
    images = pdf2image.convert_from_path(pdf_path)
    for idx, image in enumerate(images):
        image.save('%s/%03d.jpg' % (image_path, idx), 'JPEG')

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Convert PDF to images")
    arg_parser.add_argument('--pdf', dest='pdf_path', required=True)
    arg_parser.add_argument('--img', dest='image_path', required=True)
    args = arg_parser.parse_args()
    convert_pdf_to_image(args.pdf_path, args.image_path)
