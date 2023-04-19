# detect counts of all medical keywords in data set

import sys
from collections import Counter

zh_txt = open('./data/keywords/keywords.zh', encoding='utf-8').read().split('\n')
en_txt = open('./data/keywords/keywords.en', encoding='utf-8').read().split('\n')

# search keywords in english or chinese
lang = sys.argv[1]
# data file
data = sys.argv[2]

dataset = open(data, encoding='utf-8').read().split('\n')

if lang == "zh":
    keywords = zh_txt
elif lang == "en":
    keywords = en_txt

c = Counter()
for l in dataset:
    for k in keywords:
        if k in l:
            c[k] += 1
for i in c.items():
    print(i)