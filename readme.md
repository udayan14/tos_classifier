### Introduction

I use spacy(https://spacy.io/) as my ML/NLP library of choice.
Code is split up between three notebooks. The descriptions are as follows

1) preprocess.ipynb -> This notebook reads in the json files from https://github.com/tosdr/tosdr.org/tree/master/api/1/service
						It then extracts the relevant parts and stores the result in ./data/data.pkl

2) setup.ipynb      -> This notebook splits the data.pkl into training(80%) and validation(20%) sets and writes them to the disk in a binary format.

3) test_model.ipynb -> This notebook is to see our model in action. Do try it out.

You don't need to run (1) and (2), as I have supplied all the relevant data in ./data/ and the trained model in ./output/

### Installation

The relevant python3 packages required are mentioned in requirements.txt
If you have a GPU, and wish to actually train the model, follow the instructions at https://spacy.io/usage ; Don't forget to tick the train models button.
You need to download "en_core_web_sm".

### Model and Training

The actual training is all handled by spacy. We define the architecture and model parameters in "base_config.cfg" file.
Run this command to generate an actual "config.cfg" file from the "base_config.cfg" file. Spacy fills in all the parameters which we don't set with default values
$ python3 -m spacy init fill-config base_config.cfg config.cfg

To start training, run the following command
$ python -m spacy train config.cfg --output ./output

You will see the training statistics and the model will be saved in ./output/

The model I have submitted is a simple model. It is basically a bag of words + Neural Network model.
I tried using transformers, but ran into memory issues. We just need to update our base_config.cfg to use a different architecture (super easy)

My model classifies a sentence into one of the 4 categories {good, bad, neutral, blocker} and achieves a accuracy of 87%
This can definitely be improved as I used a very simple model and trained on a CPU.

### Testing

Use test.py to give new terms of service to the model and see how it performs.
There are a few sample sentences in "test_model.ipynb" picked from Facebook and Twitter ToS.
Run the code as

$ python3 test.py

The code expects a block of text and will write out the result to result.json

