#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from xpinyin import Pinyin
import os
import sys
import pdb
import re


PREFIX_NAME = ''
LINK_SEP = '_'


def walk_rename(dir_name):
    pinyin_converter = Pinyin()
    for dirpath, dirnames, filenames in os.walk(dir_name):
        for filename in filenames:
            # ignore hide file
            if filename.startswith('.'):
                continue

            # filename= '有在震mobile'
            filename_without_ext = filename.split('.')[0]
            file_ext = filename.split('.')[1]

            if file_ext == 'jpeg':
                file_ext = 'jpg'

            filename_without_ext = re.sub(
                r'([a-zA-Z]+)', LINK_SEP + r'\1', filename_without_ext
            )
                
            res = pinyin_converter.get_pinyin(filename_without_ext, '')
            res = re.sub(r'[_\s-]{2,}', '', res)
            res = re.sub(r'^[_\s-]+', '', res)
            res = re.sub(r'@2x$', '', res)
            res += '.' + file_ext

            # TODO dist folder
            src_path = os.path.join(dirpath, filename)
            dest_path = os.path.join(dirpath, res)
            print(src_path + '->' + res)
            os.rename(src_path, dest_path)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit(-1)
    if len(sys.argv) > 2:
        PREFIX_NAME = sys.argv[2]
    if len(sys.argv) > 3:
        LINK_SEP = sys.argv[3]

    for dir_name in sys.argv[1:]:
        walk_rename(dir_name)
