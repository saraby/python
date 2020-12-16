""" 
Group 1. Collaboration with Klara, Marije, Sarab.

"""

import collections

def get_word_counts(docs):

	"""
	use the Collections python standard librar to count the words in the documents
	docs = [[w1,w2], [w4,w2,w3,w1] ....]

	restrictions:
	1) you have to use Collections
	2) you have 4 lines of code, including return statement
	"""

	return collections.Counter([w for doc in docs for w in doc])