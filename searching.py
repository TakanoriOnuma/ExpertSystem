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

# ルールの作成
rules = {}
for line in line_rules:
    idx_If = line.find(u'If')
    R = line[0:idx_If].strip()
    idx_Then = line.find(u'Then')
    str_If = line[idx_If + 2:idx_Then].strip()
    list_If = str_If.split(u',')
    for i in range(len(list_If)):
        list_If[i] = list_If[i].strip()
    str_Then = line[idx_Then + 4:].strip()
    rules[R] = {'If':list_If, 'Then':str_Then}

# 入力情報の作成
f = io.open('info.dat', 'r', encoding = 'utf_8_sig')
list_info = []
for line in f:
    list_info.append(line[line.find('('):].strip())

# X情報の取得
word = list_info[0][1:-1]
check_words = [u'は', u'の'];
idx = len(word)
for ch_word in check_words:
    ch_idx = word.find(ch_word)
    if ch_idx == -1:
        ch_idx = len(word)
    if idx > ch_idx:
        idx = ch_idx

word_X = word[:idx]

# 入力情報をXに置き換え
for i in range(len(list_info)):
    list_info[i] = list_info[i].replace(word_X, u'X')

for R in rules:
    print R, ':',
    for li in rules[R]['If']:
        print li, ',',
    print rules[R]['Then']

for li in list_info:
    print li

isChange = True
while isChange:
    isChange = False
    for R in rules:
        isAllApply = True
        for rule in rules[R]['If']:
            if (rule in list_info) == False:
                isAllApply = False
                break

        if isAllApply:
            print R, "is OK."
