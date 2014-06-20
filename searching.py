# -*- coding: utf-8 -*-

import io

line_rules = []
f = io.open('animal.rule', 'r', encoding = 'utf_8_sig')

line = f.readline()
while line:
    if line.startswith(u'R', 0, 1):
        break
    line = f.readline()

# ルールを分割
while line:
    string = line[0:-1]
    line = f.readline()
    while line.startswith(u'R', 0, 1) == False and line:
        string += line[0:-1]
        line = f.readline()
    line_rules.append(string)

for r in line_rules:
    print r
