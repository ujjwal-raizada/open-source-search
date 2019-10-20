import os
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

from .utils import *
from .preprocessor import preprocess


def generate_summary(file_name):
    """
    Generates short summary for the given text
    :param file_name: String representing the document file name to be summarized
    :return String consisting of the summarized text
    """

    # Take sample text from database
    file_dir = os.listdir(CORPUS)
    text = ""
    file_path = file_name
    with open(os.path.join(CORPUS, file_path), 'r', encoding='utf-8') as f:
        text = f.read()
    f.close()

    sentences = sent_tokenize(text)
    filtered_sentences = []
    for sentence in sentences:
        filtered_sentences.append(sentence.translate(str.maketrans("","", string.punctuation)))
    sentences = filtered_sentences
    list_of_words = word_tokenize(text)

    #Remove stopwords from the set of words
    stop_words = set(stopwords.words('english'))
    words_filtered = []
    for word in list_of_words:
        if word not in stop_words:
            words_filtered.append(word)

    # Create frequency table
    frequency_table = {}
    for word in words_filtered:
        frequency_table[word] = 0

    for word in list_of_words:
        if word in frequency_table.keys():
            frequency_table[word] += 1

    # Calculate rank for each sentence
    sentence_rank = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        score = 0
        for word in words:
            if word in frequency_table.keys():
                score += (frequency_table[word] / len(sentence))
        sentence_rank.append(score)
    
    # Calculate average score
    average = 0
    for x in range(len(sentence_rank)):
        average += sentence_rank[x]
    average = average / len(sentence_rank)

    threshold = 1.5 * average

    # Generate summary based on scores
    result = ""
    for x in range(len(sentence_rank)):
        if sentence_rank[x] > threshold:
            if(len(sentences[x]) > 3):
                result += sentences[x]
                result += ". "

    return result


if __name__ == "__main__":
    print(generate_summary('terminal.md'))