import os
import pickle
from utils import *

def save_parse_file(document):
    """
    Saves the list of parsed document in a file stored in the variable PARSED_DOC_FILE.

    @params:
        document: String containing parsed file name
    """
    if os.path.exists(os.path.join(INDEX_PATH, PARSED_DOC_FILE)):
        with open(os.path.join(INDEX_PATH, PARSED_DOC_FILE), 'rb') as f :
            parsed_doc_list = pickle.load(f)
    else :
        parsed_doc_list = []
    
    if (document not in parsed_doc_list) :
        parsed_doc_list.append(document)
    
    with open(os.path.join(INDEX_PATH, PARSED_DOC_FILE), 'wb') as f:
        pickle.dump(parsed_doc_list, f)
    

def send_file(file_list):
    """
    Sends unparsed files to nltk module to create Term Incidence matrix

    @param:
        file_list: List containing files to be send to the parser.
    @returns:
        resp['status'] = HTML status code
        resp['message'] = Detailed message associated with the status code
    """
    resp = {
        "status": False,
        "message": "",
        "doc_text" : {},
    }

    unparsed_doc = file_list['files']
    doc_text = {}

    for document in unparsed_doc:    
        with open(os.path.join(CORPUS, document), 'r') as f:
            doc_text[document] = f.read()
    
        save_parse_file(document)
    
    resp['status'] = True
    resp['message'] = "Files were parsed successfully"
    resp["doc_text"] = doc_text
    return resp

if __name__ == "__main__":
    pass
