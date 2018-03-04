from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


ps = PorterStemmer()

example_words = ["voice", "voicing", "voiced", "voices"]

for w in example_words:
        print (ps.stem(w))

#maynotneed because we have wordnet
