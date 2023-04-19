# split data into train, dev, and test sets

import random, csv
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


SEED = 1234
np.random.seed(SEED)

zh_txt = open('canopy.zh', encoding='utf-8').read().split('\n')
en_txt = open('canopy.en', encoding='utf-8').read().split('\n')

raw_data = {'Chinese': [line for line in zh_txt],
            'English': [line for line in en_txt]}

df = pd.DataFrame(raw_data, columns=['Chinese', 'English'])

train, test = train_test_split(df, test_size=0.2)
valid, test = train_test_split(test, test_size=0.5)

train.to_csv('train.csv', quoting=csv.QUOTE_ALL, index=False)
valid.to_csv('dev.csv', quoting=csv.QUOTE_ALL, index=False)
test.to_csv('test.csv', quoting=csv.QUOTE_ALL, index=False)