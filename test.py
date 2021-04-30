import spacy
from collections import defaultdict
import pprint
import json

def predict(d):
    a = d['A']
    b = d['B']
    
    if (a<0.5) and (b<0.5):
        return "good"
    elif (a>=0.5) and (b<0.5):
        return "neutral"
    elif (a<0.5) and (b>=0.5):
        return "bad"
    elif (a>=0.5) and (b>=0.5):
        return "blocker"

## Model for text classification
nlp = spacy.load("./output/model-best")

## Standard spacy english model for splitting text into sentences
english = spacy.load("en_core_web_sm")


tos = input("Enter the required terms of service to check:")

doc = english(tos)
## splitting input into sentences
l = [s.text for s in doc.sents]

## Store counts
d = defaultdict(int)
output = []

for doc in nlp.pipe(l):
    label = predict(doc.cats)
    d[label] += 1
    temp_dict = {}
    temp_dict['quoteText'] = doc.text
    temp_dict['verdict'] = label
    output.append(temp_dict)

pprint.pprint(d)


output_dict = {}

output_dict['stats'] = d
output_dict['points'] = output

with open("result.json","w") as outfile:
    json.dump(output_dict,outfile)



































