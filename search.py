from src.tf_idf import calculate_tfidf


def main():
    while (True):
        print()
        query = input("Enter Search Query: ")

        if (query.lower() == "exit"):
            break

        result = calculate_tfidf(query, 10)
        result.sort(reverse=True)

        print ("Result(s): ")
        print ()

        for index, (score, result) in enumerate(result):
            print (index+1, result)


if __name__ == "__main__":
    main()