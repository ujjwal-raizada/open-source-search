# Open Source Search Engine

**A text based search engine.** <br>
This search engine will crawl through **README** files of various Github projects on the internet and store them as <u>documents</u> for our retrieval system. Each document is then indexed and stored for future use. Based on the query by the user, relevant results are returned to the user based on some ranking (to be included later) of documents.

## Getting Started

* Python (**preferably version 3.7**)
* Pip and Pipenv
* Git

## Installation

* Clone the repo using this command in your preferred directory
```git 
git clone https://www.github.com/PranjalGupta2199/open-source-search.git
```
* Change your working directory to the repo's codebase 
```bash
cd open-source-search
```
* Create and install the dependencies using **Pipenv** and move to the **src/** directory
```bash
pipenv install
pipenv shell
cd src/
```
* Create a python terminal to install **nltk** dependencies 
```python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> exit()
```
* Run the **search.py** file to make query.
```bash
python search.py
```


## Team:
* [Daksh Yashlaha](https://github.com/tufty-123)&nbsp;&nbsp;
* [Pranjal Gupta](https://github.com/PranjalGupta2199) &nbsp; &nbsp;&nbsp; &nbsp;
* [Satyam Mani](https://github.com/sat13mani) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* [Ujjwal Raizada](https://github.com/ujjwalrox) &nbsp;&nbsp;&nbsp;
