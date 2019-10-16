from nltk import *
from nltk.corpus import stopwords
from collections import Counter
import math
import numpy as np


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


def calculate_tfidf(query, documents):
    """
    Calculates the tf-idf score between the query and each document and returns them
    :param query: The text which is to be compared with other documents
    :param documents: An array of documents
    :return An array containing scores based on comparision of query with each document
    """    

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
    result = []
    for vector in documents_vector:
        score = np.dot(vector, query_vector)
        result.append(score)

    return result


if __name__ == "__main__":
    query = "There are a lot of people on the bus"
    documents = ["The bus is full of people", "We are going on a vacation", "The bus is red in color"]
    
    preprocessed_query = preprocess(query)
    preprocessed_documents = []

    for document in documents:
        preprocessed_documents.append(preprocess(document))

    print(calculate_tfidf(preprocessed_query, preprocessed_documents))