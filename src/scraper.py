import requests
import time
import os
from bs4 import BeautifulSoup
import utils

def get_document(repo_id):
    '''
    Downloads README file from the Github trending repositories and 
    saves in the directory specified in CORPUS. 

    :param 
        repo_id: String of the form <username>/<repoName>
    :return
        Integer denoting the status of exit (0 for success and 1 otherwise)
    '''

    repo_url = "https://www.github.com/" + (repo_id)
    resp = requests.get(url=repo_url)

    if (resp.status_code == 200):
        resp_content = resp.content
        parser = BeautifulSoup(resp_content, "html.parser")
        

        text = parser.find('div', id='readme').find('div', {'class' : 'Box-body'}).find('article').getText()

        file_name = repo_id.split('/')[-1]+'.md'
        file_path = os.path.join(utils.CORPUS, file_name)

        if (os.path.exists(file_path)):
            print ("This file already exists in the corpus.\n")
        else :
            with open(file_path, 'wb') as f:
                f.write(str.encode(text))
            print ('Downloaded README: {}\n'.format(file_name))

    elif (resp.status_code == 429):
        while (requests.get(repo_url, timeout=20).status_code != 429):
            time.sleep(15)
        get_document(repo_id)
    
    elif (resp.status_code == 404):
        return 1

    else :
        print (requests.get(url=repo_url).status_code)
        print ("There was some error while downloading README. Response Status Code is : ", resp.status_code)
        return 0

    return 1



def get_repo_list(site, index):
    '''
    Used for getting the repositories in the pageIndex provided by index variable.
    Then calls get_document function to download README.

    :param
        site: String containing the site url
        index: Integer used in paging of the site_url

    :return
        Integer denoting the status of exit (0 for success and 1 otherwise)
    '''
    resp = requests.get(site.format(index), timeout=20)

    if (resp.status_code == 200):
        resp_content = resp.content
        parser = BeautifulSoup(resp_content, "html.parser")
        ul_tag = parser.find('ul', {'class' : 'repo-list'})

        print ("Getting repo-list from site : {}\n".format(site.format(index)))
        for li_tag in ul_tag.findAll('li'):
            try:
                repo_id = li_tag.find('h3').get_text().strip('\n')
                print ("Found : {}".format(repo_id))
                if (get_document(repo_id) == 0):
                    return 0
            except:
                ## If the tag doesn't contain h3 tag
                break
        
        print ("---------------Done--------------------")

    elif (resp.status_code == 429):
        print ("Too many requests ! Waiting for the server to respond...")

        while (requests.get(site.format(index), timeout=20).status_code != 429):
            time.sleep(15)
        get_repo_list(site,index)

    else :
        print ("There was some error while scraping. Response Status Code is : ", resp.status_code)
        return 0

    return 1


def scrape_site():
    '''
    Wrapper function for scraping github site.
    utils.sites is a list of urls which are being scraped.
    '''
    for site in utils.sites:
        pageIndex = 1
        while (get_repo_list(site, pageIndex) == 1):
            pageIndex += 1



if __name__ == '__main__':
    scrape_site()


