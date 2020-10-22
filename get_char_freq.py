from collections import Counter
import _pickle as cp
import pickle;
import numpy as np
import codecs

def normalize(d, target=1.0):
  raw = sum(d.values())
  factor = target/raw
  return {key:value*factor for key,value in d.items()}# iteritems for  python 2.7

filename ='./data/newsgroup/khmergroups.txt'
with codecs.open(filename, encoding='utf-8') as f:
	c = Counter()
	for x in f:
		c += Counter(x.strip())
print(c)
d = dict(c)
print(d,sum(d.values()))
d = normalize(d)
print(d,sum(d.values()))

with open("./data/models/char_freq.cp",'wb') as f:
	cp.dump(d,f)
