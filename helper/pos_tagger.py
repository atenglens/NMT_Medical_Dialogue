# uses spacy to detect parts of speech: nouns, adjectives, verbs

import spacy, collections, sys
import pandas as pd

nlp = spacy.load('zh_core_web_md')

filepath = sys.argv[1]
text = open(filepath, encoding='utf-8').read()
document = nlp(text)

# count nouns
nouns = [token.lemma_ for token in document if token.pos_ == 'NOUN']
nouns_tally = collections.Counter(nouns)
print('NOUNS = ' + str(sum(nouns_tally.values())))

# count adjs
adjs = [token.lemma_ for token in document if token.pos_ == 'ADJ']
adjs_tally = collections.Counter(adjs)
print('ADJS = ' + str(sum(adjs_tally.values())))

# count verbs
verbs = [token.lemma_ for token in document if token.pos_ == 'VERB']
verbs_tally = collections.Counter(verbs)
print('VERBS = ' + str(sum(verbs_tally.values())))