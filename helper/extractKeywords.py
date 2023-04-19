# extract the lines from data set that contain medical keywords

import json, operator, random
import numpy as np

DATASET_LEN = 2725990
  
# Opening JSON file
f = open("train_data.json")
f2 = open("keywords.json")
  
# returns JSON object as a dictionary
data = np.array(json.load(f))
keywords = json.load(f2)

print("[")
for sample in data:
	if any(k in sample[0] for k in keywords):	
		print(repr(str(sample) + ","))
	elif any(k in sample[1] for k in keywords):
		print(repr(str(sample) + ","))
print("]")

# Closing file
f.close()