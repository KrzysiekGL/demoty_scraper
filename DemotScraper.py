##Webscraper for site: demotywatory.pl
##Scrapping img files
import requests
import urllib.request
import time
from bs4 import BeautifulSoup as bs4bs
import re
import os

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
