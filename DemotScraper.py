##Webscraper for site: demotywatory.pl
##Scrapping img files
import requests
import urllib.request
import time
from bs4 import BeautifulSoup as bs4bs
import re
import os

print('How many pages to sracpe?')
pagesIsANumber = False
while not pagesIsANumber:
    pages = input()
    pagesIsANumber = re.search('^([1-9][0-9]*)\s*$', pages)
    if pagesIsANumber:
        print('Scrapping ', pages, ' pages of demots')
        try:
            pages = int(pages)
        except:
            print("Couldn't convert 'pages' var into int type. Terminating program.")
            sys.exit()
    else: print('Wrong number of pages. Please, use the number between 1 and infinity:')

for page in range(1,pages+1):
    time.sleep(3)
    url = 'https://demotywatory.pl/page/' + str(page)
    response = requests.get(url)
    print('page number ', page, ' response ', response)
    soup = bs4bs(response.text, 'lxml')




'''
url = 'https://demotywatory.pl/'
response = requests.get(url)
print(response)

soup = bs4bs(response.text, 'html.parser')

imgTable = soup.findAll('img')
for i in range(len(imgTable)):
    oneATag = imgTable[i]
    oneSrc = oneATag['src']
    searchForImg = re.search('^https://img.*jpg$', oneSrc)
    if searchForImg:
        ##prepare a directory for a new file
        newDir = '/tmp/demot/' + oneSrc[oneSrc.find('/uploads')+1:oneSrc.rfind('/')+1]
        #print(newDir)
        if not os.path.isdir(newDir):
            os.makedirs(newDir)
        ##download a file
        print('Downloading img file: ', oneSrc)
        urllib.request.urlretrieve(oneSrc, '/tmp/demot/' + oneSrc[oneSrc.find('/uploads')+1:])
        time.sleep(3)
'''
