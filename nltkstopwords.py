from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text = "This is an example of a tweet from which we would like to remove words that are unnecessary in the data analytic algorithm we will deploy"
stop_words = set(stopwords.words("english"))
#english stopwords already defined by nltk

words = word_tokenize(example_text)

filtered_text = []
for w in words:
    if w not in stop_words:
        filtered_text.append(w)

#alternatively

filtered_text = [w for w in words if not w in stop_words]

print (filtered_text)
