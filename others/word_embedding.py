from gensim.models import Word2Vec
sentences = [['data', 'science'], ['vidhya', 'science', 'data', 'analytics'],['machine', 'learning'], ['deep', 'learning']]

# train the model on your corpus  
model = Word2Vec(sentences, min_count = 1)

print model.similarity('data', 'science')
#0.11222489293

print model['learning']  

"""
(0, 1) 0.345205016865
(0, 4) ... 0.444514311537
(2, 1) 0.345205016865
(2, 4) 0.444514311537
"""