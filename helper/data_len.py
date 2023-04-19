# calculate average sample and sentence length of dataset

import re

data = ""
corpus = open(data, encoding='utf-8').read().split('\n')

# function to calculate the average sentence length across a corpus
def avg_len(text):
	total_words = 0
	total_sents = 0
	for line in text:
		sentences = re.split('[.?!]', line)
		words = line.split(" ")
		# if the last value in sentences is an empty string
		if (sentences[len(sentences)-1] == ""):
			total_sents += (len(sentences) - 1)
		else:
			total_sents += len(sentences)
		total_words += len(words)
	sent_len = total_words / total_sents
	sample_len = total_words / len(text)
	return sent_len, sample_len

sent_len, sample_len = avg_len(corpus)
out_file = open("datasets_avglen.txt", "a", encoding='utf-8')
out_file.write(data + " " + "{:.2f}".format(sent_len) + "\n")
out_file.write(data + " " + "{:.2f}".format(sample_len) + "\n")
out_file.close()
