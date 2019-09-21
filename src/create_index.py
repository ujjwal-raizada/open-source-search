from file_checker import check_new
from file_sender import send_file
from preprocessing import preprocess
from build_index import Index
from scraper import scrape_site

def create_index(doc_token):
    """
    Wrapper function which updates the our inverted index matrix. 

    @param: Dictionary with doc_name and occurrence of different words in it.
    """
    obj = Index('db')

    for doc_name, word_freq in doc_token.items():
        obj.update_index(doc_name, word_freq)

    # print(obj.print_index())
    # print(obj.get_compound_result(['java']))


def get_doc_tokens():
    """
    Wrapper function which checks for new documents in the corpus and preprocess it
    and then updates the inverted index matrix.

    @return: Dictionary containing document name with its corresponding occurrence of different
        words.
    """

    new_files = check_new()
    print (new_files)
    doc_wordFreq = {}

    if (new_files['status']) :
        file_text = send_file(new_files)

        for doc_name, doc_text in file_text['doc_text'].items():
            temp_counter = preprocess(doc_text)
            doc_wordFreq[doc_name] = temp_counter
    
    return create_index(doc_wordFreq)


if __name__ == '__main__':
    scrape_site()
    get_doc_tokens()
