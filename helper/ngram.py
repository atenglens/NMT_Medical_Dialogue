# counts all unigrams, bigrams, trigrams in corpus


import nltk, re, string, collections
from nltk.util import ngrams # function for making ngrams

data = ""
with open(data, "r", encoding='utf-8') as file:
    text = file.read()

# get rid of punctuation (except periods!)
punctuationNoPeriod = "[" + re.sub("\.","",string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, "", text)
text = text.lower()

# tokenize words
tokenized = text.split()

# unigrams
unigrams = ngrams(tokenized, 1)
# frequency of each bigram in corpus
unigramFreq = collections.Counter(unigrams)
# print("Unigram Frequency")
# print(unigramFreq)
unigramtop20 = unigramFreq.most_common(20)
print("Top 20 Unigrams")
for gram in unigramtop20:
    gram0 = str(gram[0])
    gram0 = re.sub(",", "", gram0)
    print(gram0 + " " + str(gram[1]))

# bigrams
bigrams = ngrams(tokenized, 2)
# frequency of each bigram in corpus
bigramFreq = collections.Counter(bigrams)
# print("Bigram Frequency")
# print(bigramFreq)
bigramtop20 = bigramFreq.most_common(20)
print("Top 20 Bigrams")
for gram in bigramtop20:
    print(str(gram[0]) + " " + str(gram[1]))

# trigrams
trigrams = ngrams(tokenized, 3)
# frequency of each bigram in corpus
trigramFreq = collections.Counter(trigrams)
# print("Trigram Frequency")
# print(trigramFreq)
trigramtop20 = trigramFreq.most_common(20)
print("Top 20 Trigrams")
for gram in trigramtop20:
    print(str(gram[0]) + " " + str(gram[1]))
