# calls Google Translate API to generate translations
# file containing sentences should be in a json format

import json
from google.cloud import translate_v2 as translate
import os
import six
import html
from tqdm import tqdm
import sys

INPUT = sys.argv[1]
OUTPUT = sys.argv[2]
START = int(sys.argv[3])
CRED_PATH = "your_cred.json"

f = open(INPUT)
data = json.load(f, strict=False)
LEN = len(data)
out = []

for i in tqdm(range(START, LEN)):
  translation = []
  for t in data[i]:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CRED_PATH
    translate_client = translate.Client()
    if isinstance(t, six.binary_type):
        t = t.decode("utf-8")
    result = translate_client.translate(t, target_language="en")
    translation.append(html.unescape(result["translatedText"]))
  out.append(translation)
  if (i+1) % 2 == 0:
    out_f = open(OUTPUT, "a", encoding='utf-8')
    out = map(str, out)  
    for line in out:
      out_f.write(line + "\n")
    out_f.close()
    out = []
    
f.close()