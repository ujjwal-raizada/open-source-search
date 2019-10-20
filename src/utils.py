import os

cwd = os.getcwd()
CORPUS = os.path.join(cwd,'corpus')
PREPROCESSED_DATA = os.path.join(cwd, 'preprocessdata')
sites = [
    "https://github.com/search?p={}&q=stars%3A%3E0&s=stars&type=Repositories",  \
    "https://github.com/search?o=desc&p={}&q=stars%3A%3E1&s=forks&type=Repositories"]
