# I will send the request to the web site by using library name "requests" (pip install requests)
import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    '''takes in a url string and returns an integer (the number of citations needed.)'''

    response=requests.get(url)

    wiki_page = response.text # take data as byte 

    soup = BeautifulSoup(wiki_page,'html.parser')  # to convert/parse data from byte to html element
    # print (soup)

    # start saerching ->

    citations_count = len(soup.find_all('a', title ='Wikipedia:Citation needed'))

    return citations_count

def get_citations_needed_report(url):
    '''takes in a url string and returns a report string, the string should be formatted with each citation listed in the order found.'''

    response = requests.get(url)

    wiki_page = response.text

    soup = BeautifulSoup(wiki_page,'html.parser')

    paragraphs = soup.findAll(name='p')

    for i in paragraphs:

        if i.find(title='Wikipedia:Citation needed'):
            with open('paragraph_needed_citation.tx.txt','a') as f:
                f.write(i.text +'\n')



