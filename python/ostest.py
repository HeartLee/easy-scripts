#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

for root, dirs, files in os.walk('../shou'):
    for name in files:
        print('==='+name+'===')
    for name in dirs:
        print('--'+name+'--')