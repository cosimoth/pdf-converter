import nltk

words = set(nltk.corpus.words.words())
sent = "我是“abc”12d]."
str = " ".join(w for w in nltk.wordpunct_tokenize(sent) \
     if w.lower() in words or not w.isalpha())
print(str)