from nltk import word_tokenize, pos_tag
text = "This is just learning Natural Language Processing on Analytics"
tokens = word_tokenize(text)
print pos_tag(tokens)
