import nltk

VALID_PoS = ['JJ','JJR','JJS','NN','NNS']
#VALID_PoS = ['NN', 'NNP', 'NNPS', 'NNS']


def tokenize(sentence):
      #print "Tokenizing: ", sentence
      tokens = nltk.word_tokenize(sentence)
      tagged = nltk.pos_tag(tokens)
      return [tag[1] for tag in tagged if is_valid(tag)]

def is_valid(tag):
      return tag[1] in VALID_PoS

def tokenize_wiki(sentence):
      return [tag[0] for tag in nltk.pos_tag(sentence) if is_valid(tag)]
