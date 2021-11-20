#!/usr/local/bin/python3

import argparse
import re

chapter_patterns = [re.compile(r'^[第][一二三四五六七八九十]+[章]'), re.compile(r'^[0-9]+[、]')]

def convert_txt_to_md(txt_path, md_path):
    with open(txt_path, 'r') as txt, open(md_path, 'w') as md:
        for no, line in enumerate(txt.readlines()):
            chapter_prefix = ''
            if no > 128:
                for idx, chapter_pattern in enumerate(chapter_patterns):
                    if chapter_pattern.search(line):
                        chapter_prefix = (idx + 1) * '#' + ' '
            md.write(chapter_prefix + line + '\r\n')

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Convert text to markdown")
    arg_parser.add_argument('--txt', dest='txt_path', required=True)
    args = arg_parser.parse_args()
    convert_txt_to_md(args.txt_path, args.txt_path + '.md')