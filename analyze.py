import tokenizer
import json, collections, cPickle
from sklearn.linear_model import SGDClassifier

f = open('reviews_Electronics.json', 'r')
#f_out = open('reviews_Musical_Out.txt', 'wb')

vector_indeces = ['len', 'JJ','JJR','JJS','NN','NNS']
vectors = []
votes = []
cnt = 0

for line in f:
	cnt += 1
	if((cnt % 100) == 0):
		print str(cnt)
	content = json.loads(line)
	if (content['helpful'][1] < 15):
		continue
	tagged = tokenizer.tokenize(content['reviewText'])
	counter = list(collections.Counter(tagged).most_common())
	wordCount = len(content['reviewText'].split())
	relativ_count = []
	reviewVector = collections.OrderedDict.fromkeys(vector_indeces, float(0))
	reviewVector['len'] = float(wordCount)
	for (tag, count) in counter:
		reviewVector[tag] = count / float(wordCount)
	vectors.append(list(reviewVector.values()))
	try:
		votes.append(int((content['helpful'][0] / float(content['helpful'][1]))*1000))
	except:
		votes.append(0)

print 'Processed ', str(cnt), ' lines.'
print 'Making model'

clf = SGDClassifier(loss="hinge", penalty="l2")
clf.fit(vectors, votes)
print 'Finished model. Saving ...'
with open('reviews_elec_model.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)  
print 'FINISH'

