from nltk import *
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import Counter

import math
import numpy as np
import os

from .utils import *
from .preprocessor import preprocess


def fetch_documents():
    """
    Gets the list of documents and their associated data from the text files in the corpus folder
    :return array containing data associated with each file in each index, in a sorted fashion
    """
    
    # List of documents
    file_dir = os.listdir(CORPUS)
    file_dir.sort()
    documents = []

    #Save text associated with each file in the array
    for path in file_dir:
        reader = open(os.path.join(CORPUS, path))
        text = ""
        for line in reader:
            text += line
        documents.append(text)
        reader.close()

    return documents


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
    :param documents: An array of documents
    :param no_of_docs: Required number of search results to be returned
    :return An array containing scores based on comparision of query with each document
    """    

    #Get the list of documents and their data
    documents = fetch_documents()

    #Preprocess Documents
    preprocessed_documents = []
    for document in documents:
        preprocessed_documents.append(preprocess(document))

    #Preprocess Query
    query = expand_query(query)
    preprocessed_query = preprocess(query)

    query = preprocessed_query
    documents = preprocessed_documents

    #Find the list of unique words in the document
    list_of_words = []
    for word in query:
        if word not in list_of_words:
            list_of_words.append(word)
    
    for document in documents:
        for word in document:
            if word not in list_of_words:
                list_of_words.append(word)

    N = len(documents) + 1

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

    #Generate vector for each document
    copy_documents = documents
    documents_vector = []
    for document in documents:
        doc_vector = []
        for word in list_of_words:
            #Calculate term frequency
            tf = 0
            for term in document:
                if term == word:
                    tf = tf + 1

            #Calculate document frequency
            df = 0
            if word in query:
                df = df + 1
            for copy_document in copy_documents:
                if word in copy_document:
                    df = df + 1
            
            #Calculate tf-idf
            idf = math.log(N/df)
            tfidf = tf*idf
            doc_vector.append(tfidf)

        documents_vector.append(doc_vector)

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
    query = 'web development'
    print(calculate_tfidf(query, 3))