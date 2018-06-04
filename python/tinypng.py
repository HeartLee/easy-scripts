#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import pdb
import re
import tinify


tinify.key = "XJXH8HcYhLMGsTWOkkIbcFXmKpDJfk0q"


def walk_dir(dir_name):
    count = 0
    print('--- '+ dir_name +'-----')
    print('------ tiny task start ---------')
    for dirpath, dirnames, filenames in os.walk(dir_name):
        for filename in filenames:
            if re.search(r'\.(jpg|png|jpeg)$', filename) is None:
                continue

            src_path = os.path.join(dirpath, filename)
            try:
                source = tinify.from_file(src_path)
                print('==='+src_path+'===')
                print('- tiny finish: ' + src_path)
                source.to_file(src_path)
                print('- tiny save:  ' + src_path)
                count += 1
                print('---------count %s----------------' % count)
            except tinify.Error:
                print(tinify.Error)
    print('------ tiny task finished ---------')
    print('------ good luck ---------')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit(-1)

    for dir_name in sys.argv[1:]:
        walk_dir(dir_name)
