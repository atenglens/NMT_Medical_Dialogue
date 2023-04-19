import spacy, sys
from transformers import AutoTokenizer
from pywordseg import *
from collections import Counter

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
spacy_en = spacy.load('en_core_web_sm')

source_file = sys.argv[1]
target_file = sys.argv[2]
input_file = sys.argv[3]

zh_txt = open(source_file, encoding='utf-8').read().split('\n')
en_txt = open(target_file, encoding='utf-8').read().split('\n')
zh_en = open(input_file, encoding='utf-8').read().split('\n')

# declare the segmentor
seg = Wordseg(batch_size=64, device="cuda:0", embedding='elmo', elmo_use_cuda=True, mode="TW")
segments = seg.cut(zh_txt)

zh_tokens = []
en_tokens = []

for i in range(len(zh_txt)):
    zh_sentence = segments[i]
    en_sentence = spacy_en.tokenizer(en_txt[i])
    zh_tokens.append(zh_sentence)
    en_tokens.append([tok.text for tok in en_sentence])

c = Counter()
for i in range(len(zh_tokens)):
    tokens = zh_en[i].split(' ')
    for t in tokens:
        split = t.split('-')
        src_index = int(split[0])
        trg_index = int(split[1])
        pair = '(' + zh_tokens[i][src_index] + ')-(' + en_tokens[i][trg_index] + ')'
        c[pair] += 1
        
punc = "，。‘？！；、…：,.:?!';–"
for i in c.items():
    if any(char in punc for char in i[0]):
        continue
    if "(-)" in i[0]:
        continue
    print(i[0] + ', ' + str(i[1]))