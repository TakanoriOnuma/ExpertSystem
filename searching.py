# -*- coding: utf-8 -*-

import io

rule = {}
f = io.open('animal.rule', 'r', encoding = 'utf_8_sig')

line = f.readline()
while line:
    if line.startswith(u'R', 0, 1):
        break
    line = f.readline()

# ルールを分類
while line:
    R  = line[0:line.find('\t')]
    li = [line]
    line = f.readline()
    while line.startswith(u'R', 0, 1) == False and line:
        li.append(line)
        line = f.readline()
    rule[R] = li
rule[R] = li

for r in rule:
    print r,
    for word in rule[r]:
        print word,
