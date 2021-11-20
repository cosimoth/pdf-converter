#!/usr/local/bin/python3


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Convert PDF to images")
    arg_parser.add_argument('--pdf', dest='pdf_path', required=True)
    arg_parser.add_argument('--img', dest='image_path', required=True)
    args = arg_parser.parse_args()
    convert_pdf_to_image(args.pdf_path, args.image_path)