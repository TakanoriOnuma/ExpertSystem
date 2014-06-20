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
print '----------------------'

# ルールの作成
rules = {}
for line in line_rules:
    idx_If = line.find(u'If')
    R = line[0:idx_If].strip()
    idx_Then = line.find(u'Then')
    str_If = line[idx_If + 2:idx_Then].strip()
    str_Then = line[idx_Then + 4:].strip()
    print R, ':', str_If, '->', str_Then
    
