__author__ = 'kunwar'


import requests
from bs4 import BeautifulSoup

FILE = open("Config.txt","r")

def start():
    STR1 = FILE.readline().partition("url = ")
    URL= STR1[2]

    STR2 = FILE.readline().partition("root_directory=")
    ROOT = STR2[2]

    re =requests.get(URL)
    data = re.text
    soup = BeautifulSoup(data)

    for link in soup.find_all('a'):
        if link.has_attr('href'):
            var = link.get('href')
            if (("http" or "https") and "git" ) in var:
                url = link.get('href')
                clone(url, ROOT)
    return

def clone(URL, ROOT_DIRECTORY):

    import re,os, sys,urllib2
    content = urllib2.urlopen(URL).read()
    pattern = URL + ".git"
    if pattern in content:
        print pattern
        os.umask(0002)
        os.makedirs(ROOT_DIRECTORY, 0777)
        os.chmod(ROOT_DIRECTORY, 0777)
       #.path.exists(ROOT_DIRECTORY))
       #s.path.exists(ROOT_DIRECTORY):
       #akedirs(ROOT_DIRECTORY, 0755)
       #t "zumba"
       #string = "git clone %s %s" %(URL, ROOT_DIRECTORY)
       #ystem(cmd_string)
    return

start()