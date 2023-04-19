# send messages to ChatGPT and receive responses

import openai, csv

# generate text
# openai.api_key = {insert-key-here}

prompt1 = 'Translate the following Chinese text to English: '
prompt2 = 'Translate the following Chinese text to colloquial English: '
prompt3 = 'Translate the following Chinese text to English with correct English pronouns: '
csms_dev = "csms_dev.zh"
dpronouns = "dpronouns.zh"
corpus = open(csms_dev, encoding='utf-8').read().split('\n')
train100 = open("csms_train100.csv", encoding='utf-8').read().split('\n')
    
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work

### experiment 3 ###
history = []
history.append({"role": "system", "content": "You are a doctor fluent in Chinese and English who is talking to a patient."}) ### experiment 2 ###

with open('csms_train100.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        history.append({"role": "user", "content": line[0]})
        history.append({"role": "assistant", "content": line[1]})

for line in corpus:
	messages = history.copy()

	chinese_txt = prompt1 + line
	messages.append({"role": "user", "content": chinese_txt})
	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=messages
	)
	response = completion.choices[0].message.content
	print(response)