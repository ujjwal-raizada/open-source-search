from nltk import *
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import Counter

import math
import numpy as np
import os
import pickle

try:
    from .utils import *
    from .preprocessor import preprocess
except:
    from utils import *
    from preprocessor import preprocess


def expand_query(text):
    """
    Expand the input query words using wordnet corpus dataset
    :param text: The input query
    :return Text representing the expanded query
    """
    text = text.lower()
    tokens = word_tokenize(text)

    #Find synonyms to given text using corpus dataset
    synonyms = []
    for word in tokens:
        for syn in wordnet.synsets(word):
            if len(syn.lemmas()) > 3:
                for x in range(3):
                    synonyms.append(syn.lemmas()[x].name())
            else:
                for x in range(len(syn.lemmas())):
                    synonyms.append(syn.lemmas()[x].name())

    # Add synonyms to query
    for word in synonyms:
        if word in text:
            pass
        else:
            text += " "
            text += word

    return text


def calculate_tfidf(query, no_of_docs):
    """
    Calculates the tf-idf score between the query and each document and returns them
    :param query: The text which is to be compared with other documents
    :param no_of_docs: Required number of search results to be returned
    :return An array containing scores based on comparision of query with each document
    """    
    #Preprocess Query
    query = expand_query(query)
    preprocessed_query = preprocess(query)
    query = preprocessed_query

    # Pick up preprocessed data
    pickle_in = open(PREPROCESSED_DATA, 'rb')
    db = pickle.load(pickle_in)
    pickle_in.close()

    # Get data from database dictionary
    list_of_words = db['list_of_words']
    N = db['N']
    documents_vector = db['documents_vector']
    documents = db['documents']

    #Generate query vector
    query_vector = []
    for word in list_of_words:
        #Calculate term frequenct
        tf = 0
        for term in query:
            if term == word:
                tf = tf + 1

        #Calculate document frquency
        df = 0
        if word in query:
            df = df + 1
        for document in documents:
            if word in document:
                df = df + 1
        
        #Calculate tf-idf
        idf = math.log(N/df)
        tfidf = tf*idf
        query_vector.append(tfidf)

    
    #Calculate cosine similarity for each document
    scores = []
    for vector in documents_vector:
        score = np.dot(vector, query_vector)
        scores.append(score)

    file_dir = os.listdir(CORPUS)
    file_dir.sort()

    # Save tuple of form (score, document name) in an array
    document_scores = []
    for x in range(len(file_dir)):
        document_scores.append((scores[x], file_dir[x]))

    document_scores.sort(reverse=True)

    # Return k ranked documents (k = no_of_docs)
    result = []
    if len(document_scores) < no_of_docs:
        for x in range(len(document_scores)):
            result.append(document_scores[x])
    else:
        for x in range(no_of_docs):
            result.append(document_scores[x])

    return result


if __name__ == "__main__":
    query = 'react'
    print(calculate_tfidf(query, 3))