# extract the desired data from original MedDialog data set

import json, operator, random
import numpy as np

DATASET_LEN = 2725990
  
# Opening JSON file
f = open("test_data.json")
  
# returns JSON object as a dictionary
data = np.array(json.load(f))

for sample in data:
	print(sample[0][3:], sample[1][3:])

# Closing file
f.close()