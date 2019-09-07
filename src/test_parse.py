from file_checker import *
from file_sender import *
import pickle

def test_parse():
    """
    Checks the working of file_checker and file_sender modules
    """

    file_list = check_new()

    if (file_list['status']):
        a = send_file(file_list)
        print (a)

    with open(os.path.join(STORE, PARSED_DOC_FILE), 'rb') as f:
        l = pickle.load(f)
        print (l)
    
    

if __name__ == "__main__":
    test_parse()