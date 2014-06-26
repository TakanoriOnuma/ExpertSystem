# -*- coding: utf-8 -*-

import io

line_rules = []
f = io.open('food.rule', 'r', encoding = 'utf_8_sig')

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
f = io.open('info3.dat', 'r', encoding = 'utf_8_sig')
list_info = []
for line in f:
    list_info.append(line[line.find('('):].strip())

# ルールや入力データを出力
print '---------- rules ----------'
for R in rules:
    print R, ':', ', '.join(rules[R]['If']) , '->', rules[R]['Then']

print '---------- infomation ----------'
for li in list_info:
    print li
    
# X情報の取得
word_X = list_info[0][1:]
for i in range(len(list_info[0][1:-1])):
    word_X = word_X[:-1]
    flag = True
    for ch_word in list_info:
        # 先頭に同じ文字を見つけられなかったら
        if ch_word.find(word_X) != 1:
            flag = False
    if flag:
        break

check_words = [u'は', u'の'];
if word_X[-1] in check_words:
    word_X = word_X[:-1]

print 'X =', word_X

# 入力情報をXに置き換え
for i in range(len(list_info)):
    list_info[i] = list_info[i].replace(word_X, u'X')

# 推論を行う
print '---------- predict phase ----------'
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
            if (rules[R]['Then'] in list_info) == False:
                isChange = True
                list_info.append(rules[R]['Then'])
                print R, 'is OK.'
                print R, ':', ', '.join(rules[R]['If']) , '->', rules[R]['Then']

# 結論
print '---------- conclusion ----------'
result = list_info[-1].replace(u'X', word_X)[1:-1]
print result
