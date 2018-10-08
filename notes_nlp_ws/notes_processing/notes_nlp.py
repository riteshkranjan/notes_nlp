from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob

with open('train_ticketdata.csv','r') as training_corpus:
	model = NBC(training_corpus, format='csv')

with open('test_ticketdata.csv','r') as test_corpus:
	accuracy = model.accuracy(test_corpus)

def apply_nlp(data):
    print("start nlp")
    print(data)
    print("end nlp")
    return model.classify(data)
	
def get_accuracy():
    return accuracy
