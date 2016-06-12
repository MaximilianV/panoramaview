import tokenizer
import json, collections, cPickle
from sklearn.linear_model import SGDClassifier

vector_indeces = ['len', 'JJ','JJR','JJS','NN','NNS']
vectors = []
class ModelServer:
	def __init__(self, text):
		self.reviewText = text
		#with open('reviews_elec_model.pkl', 'rb') as fp:
		with open('reviews_model.pkl', 'rb') as fp:
			self.clf = cPickle.load(fp)

	def evaluate(self):
		tagged = tokenizer.tokenize(self.reviewText)
	        counter = list(collections.Counter(tagged).most_common())
       		wordCount = len((self.reviewText).split())
	        relativ_count = []
	        reviewVector = collections.OrderedDict.fromkeys(vector_indeces, float(0))
	        reviewVector['len'] = float(wordCount)
	        for (tag, count) in counter:
	                reviewVector[tag] = count / float(wordCount)
		vec = []
		vec.append(list(reviewVector.values()))
		print vec
		return self.clf.predict(vec)
