# -*- coding: utf-8 -*-

import io

f = io.open('animal.rule', 'r', encoding = 'utf_8_sig')

for line in f:
    words = line.split('\t')
    for word in words:
        print word,

