import os
import pickle
from utils import *

def check_new():
    """
    Returns the list of documents that are unparsed by the search engine backend.
    Parsed files are stored in a form of list in a binary file in the 'store' directory.

    @returns:
        resp['status'] = HTML status code
        resp['message'] = Detailed message associated with the status code
        resp['files'] = List of files which need to be parsed
    """

    resp = {
        "status": False,
        "message": "",
        "files" : [],
    }

    try:
        file_dir = os.listdir(CORPUS)
    except OSError:
        resp['message'] = "Error ! Corpus doesn't exists"
        return resp

    try:
        with open(os.path.join(INDEX_PATH, PARSED_DOC_FILE), 'rb') as f:
            parsed_doc = pickle.load(f)
    except:
        print ("Binary file doesn't exists")
        parsed_doc = []

    for document in file_dir:
        if (document not in parsed_doc):
            resp['files'].append(document)
    
    if (len(resp['files']) != 0):
        resp['status'] = True
        resp['message'] = "New files added"
    else :
        resp['status'] = False
        resp['message'] = "No new files added"
    
    return resp


if __name__ == "__main__":
    print (check_new())
