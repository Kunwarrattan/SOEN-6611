__author__ = 'kunwar'


import requests
from bs4 import BeautifulSoup

FILE = open("Config.txt","r")
STR1 = FILE.readline()
VAR = STR1.partition("url = ")
URL= VAR[2]
STR2 = FILE.readline();
print(STR2)

re =requests.get(URL);

data = re.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
