import pickle
import pathlib

import nltk

from sortedcontainers import SortedSet
from utils import * 

class Index:


    """

    This class acts as the data-structure for the inverted index.
    Provides functionality to update, search, load and dump the the index.

    """

    def __init__(self, db_name):
        
        self.db_name = db_name
        self.__inverted_index = {}
        self.load_index()

    def update_index(self, filename, token_freq):

        """

        this function updates the index with every new file insertion.

        param filename: name of the file to be inserted in the index
        param token_freq: dict with frequency ratio of words in the given file

        """

        for token, freq in token_freq.items():

            if token in self.__inverted_index.keys():
                self.__inverted_index[token].add((freq, filename))

            else:
                index_list = SortedSet()
                index_list.add((freq, filename))
                self.__inverted_index[token] = index_list

            self.dump_index()

    def get_result(self, search_keyword, num_of_result = 5):

        result = SortedSet()
        if search_keyword in self.__inverted_index.keys():
            if len(self.__inverted_index[search_keyword]) >= num_of_result:
                result = self.__inverted_index[search_keyword][0:num_of_result]
            else:
                result = self.__inverted_index[search_keyword][:]

        final_result = SortedSet()
        for tup in result:
            freq, token = tup
            final_result.add(token)
        
        return final_result

    def get_compound_result(self, keyword_list, num_of_result = 5):

        """

        This function accepts a list of keywords,
        and returns the intersection of the resultset for each of the keyword.

        @param keyword_list: list of keywords to be searched
        @param num_of_result: maximum number of results needed (default: 5)

        @return: list of result

        """

        ps = nltk.PorterStemmer()
        result = self.get_result(ps.stem(keyword_list[0]), num_of_result)

        for keyword in keyword_list:
            result = self.get_result(ps.stem(keyword), num_of_result) & result

        return result

    def load_index(self):

        """

        loads the inverted index from the binary file for persistant storage.

        """


        db_path = pathlib.Path(INDEX_PATH + self.db_name)

        if not db_path.exists():
            self.dump_index()

        with open(INDEX_PATH + self.db_name, 'rb') as file:
            self.__inverted_index = pickle.load(file)
            print ("Index Load Successful.")

    def dump_index(self):

        """
        dumps the inverted index to a binary file for persistant storage.
        """


        with open(INDEX_PATH + self.db_name, 'wb') as file:
            pickle.dump(self.__inverted_index, file)
            print ("Inverted Index Dumped Successfully.")

    def print_index(self):
        print(self.__inverted_index)
