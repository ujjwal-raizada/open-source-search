from nltk import *
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import Counter


def preprocess(text):
    """
    Preprocess the given text - performs tokenization, stemming and removes stopwords
    :param text: The input text which is to be preprocessed in form of a string
    :return array containing words in given text which are of significance
    """

    #Tokenize
    text = text.lower()
    tokens = word_tokenize(text)

    #Filter Stopwords
    stop_words = set(stopwords.words('english'))
    words_filtered = []

    for word in tokens:
        if word not in stop_words:
            words_filtered.append(word)

    #Perform Stemming
    words_stemmed = []
    ps = PorterStemmer()

    for word in words_filtered:
        words_stemmed.append(ps.stem(word))

    return words_stemmed