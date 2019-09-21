import requests
import time
from bs4 import BeautifulSoup
import utils


def get_repo_list(site, index):
    resp = requests.get(site.format(index), timeout=20)

    if (resp.status_code == 200):
        resp_content = resp.content
        parser = BeautifulSoup(resp_content, "html.parser")
        ul_tag = parser.find('ul', {'class' : 'repo-list'})

        print ("Getting repo-list from site : {}\n".format(site.format(index)))
        try:
            for li_tag in ul_tag.findAll('li'):
                try:   
                    repo_id = li_tag.find('h3').get_text()
                    print ("Found : {}".format(repo_id[1:]))
                except:
                    ## If the tag doesn't contain h3 tag
                    pass
        except:
            ## If ul.findAll('li') returns a None object
            pass
        
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
    for site in utils.sites:
        pageIndex = 1
        while (get_repo_list(site, pageIndex) == 1):
            pageIndex += 1



if __name__ == '__main__':
    scrape_site()



