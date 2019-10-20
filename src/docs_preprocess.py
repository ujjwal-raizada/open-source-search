import math
import os
import pickle

from utils import *
from preprocessor import preprocess


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
        with open(os.path.join(CORPUS, path), 'r', encoding='utf-8') as f:
            text = f.read()
            documents.append(text)
            f.close()

    return documents


def calculate_tf_idf_docs():
    #Get the list of documents and their data
    documents = fetch_documents()

    #Preprocess Documents
    preprocessed_documents = []
    for document in documents:
        preprocessed_documents.append(preprocess(document))

    documents = preprocessed_documents

    # Find the list of unique words in the document dataset
    list_of_words = []
    for document in documents:
        for word in document:
            if word not in list_of_words:
                list_of_words.append(word)

    N = len(documents) + 1

    # Generate vector for each document
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
            for copy_document in copy_documents:
                if word in copy_document:
                    df = df + 1
            
            #Calculate tf-idf
            idf = math.log(N / df)
            tfidf = tf * idf
            doc_vector.append(tfidf)
        
        documents_vector.append(doc_vector)

    #Generate database
    db = {}
    db['list_of_words'] = list_of_words
    db['N'] = N
    db['documents_vector'] = documents_vector
    db['documents'] = documents

    #Save data to persistence storage
    pickle_out = open(PREPROCESSED_DATA, 'wb')
    pickle.dump(db, pickle_out)
    pickle_out.close()


if __name__ == "__main__":
    calculate_tf_idf_docs()