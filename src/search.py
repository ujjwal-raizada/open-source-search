from build_index import Index
from create_index import get_doc_tokens

get_doc_tokens()
index_obj = Index('db')
while (True):

    print()
    query = input("Enter Search Query: ")

    if (query.lower() == 'exit'):
        break

    query_list = query.split()
    query_result = index_obj.get_compound_result(query_list)

    print("Result(s): ")
    print()

    for index, result in enumerate(query_result):
        print(index + 1, result)




