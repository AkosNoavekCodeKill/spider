import sys
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

# class Bcolors:
# Black=        0;30     Dark Gray     1;30
# Red=          0;31     Light Red     1;31
# Green=        0;32     Light Green   1;32
# Brown_Orange 0;33     Yellow        1;33
# Blue=         0;34     Light Blue    1;34
# Purple=       0;35     Light Purple  1;35
# Cyan=         0;36     Light Cyan    1;36
# Light_Gray   0;37     White         1;37
#     RED='\033[0;31m'
#     NC='\033[0m'
def get_pages(url, keyword):
    visited_urls = set()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tags = soup.find_all('a')
    urls = []
    for link in a_tags:
        linkParsed = link.get('href')
        if linkParsed != '' and linkParsed is not None:
            urls.append(linkParsed)
    pages_related = []
    for url2 in urls:
        if url2 not in visited_urls:
            visited_urls.add(url2)
            url_join = urljoin(url, url)
            print(url_join)
            if keyword is None or keyword in url_join:
                pages_related.append(f'{url2} {spider_urls(url_join, keyword)}')
        else:
            print(f'URL already visited {url2}')
    return pages_related

def first_try(url):
    # Define the XML data for the POST request
    xml_data = '''
    <methodCall>
    <methodName>system.listMethods</methodName>
    <params></params>
    </methodCall>'''

    # Set the headers to indicate the type of data being sent
    headers = {'Content-Type': 'text/xml'}

    # Make the POST request with XML data
    response = requests.post(url, data=xml_data, headers=headers)

    # Print the response text (or process it as needed)
    print(response.text)

def spider_urls(url, keyword):
    if url is None or url == '':
        url = input('Enter the url you want to scrap')

    try:
        response = requests.get(url)
        return response
    except():
        print('failed')


#get_pages(input('Url to scrape: '), input('Enter a search term: '))

#https://it.wikipedia.org/wiki/Pagina_principale



#def
# new section

def urls(out_file_sp):
    #info
    # With wordlist passed trough sh pipe
    #rl2 = sys.stdin.read().splitlines()
    #info
    # From url
    tar = 'https://it.wikipedia.org/wiki/Pagina_principale'
    url2 = get_pages(tar, None)
    res_urls = []
    bad_urls = []
    for url in url2:
        try:
            print(url)
            if requests.head(str(url)) == 200:
                res_urls.append(str(url))
        except Exception as e:
            bad_urls.append(str(e))

    open(out_file_sp, 'w').write('Good urls: \n' + '\n'.join(res_urls) + 'Broken urls: \n' + '\n'.join(bad_urls))
    print('Done')
    exit()
out_file = 'filtered_url.txt'
urls(out_file)