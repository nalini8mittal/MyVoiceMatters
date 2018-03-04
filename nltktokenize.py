import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize

#sentence tokenizing
example_text = "Hello and welcome to the tokenizing demo. Welcome to the sentencing demo."
print (sent_tokenize(example_text))

#work tokenize
print (word_tokenize(example_text))

for i in word_tokenize(example_text):
    print (i)



nltk.download()
