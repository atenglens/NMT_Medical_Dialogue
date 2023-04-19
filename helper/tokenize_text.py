# tokenizes source and target sentences and produces file in the 
# right input format for fast_align: https://github.com/clab/fast_align

import spacy, sys
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
spacy_en = spacy.load('en_core_web_sm')

source_file = sys.argv[1]
target_file = sys.argv[2]

zh_txt = open(source_file, encoding='utf-8').read().split('\n')
en_txt = open(target_file, encoding='utf-8').read().split('\n')

for i in range(len(zh_txt)):
    zh_sentence = [*zh_txt[i]]
    en_sentence = spacy_en.tokenizer(en_txt[i])
    print(" ".join([tok for tok in zh_sentence]) + " ||| " + " ".join([tok.text for tok in en_sentence]))