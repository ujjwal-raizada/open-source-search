from nltk import *
from nltk.corpus import stopwords
from collections import Counter


def preprocess(text):
	"""
	Tokenizes the given text into words and returns the number of occurences of each word in the text
	:param text:The input text file whose words are to be tokenized and counted
	:return: A Counter object containing a dictionary of words with key as word and value as their number of occurences
	"""

	text = text.lower()
	tokens = word_tokenize(text)
	
	stop_words = set(stopwords.words('english'))

	words_filtered = []

	# Remove common stopwords like 'This', 'a', etc.
	for word in tokens:
		if word not in stop_words:
			words_filtered.append(word)

	# Generate stem for each word
	words_stemmed = []
	ps = PorterStemmer()
	for word in words_filtered:
		words_stemmed.append(ps.stem(word))

	#Count occurence of each word
	result = Counter(words_stemmed)
	length_of_result = len(words_filtered)
	for data in result:
		result[data] = result[data] / length_of_result

	return result
