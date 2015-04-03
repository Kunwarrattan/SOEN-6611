__author__ = 'kunwar'


import requests
from bs4 import BeautifulSoup


FILE = open("Config.txt","r")

def FilterURL():
    STR1 = FILE.readline().partition("url = ")
    URL= bytes(STR1[2], 'utf8')

    STR2 = FILE.readline().partition("root_directory=")
    ROOT = STR2[2] # bytes(STR2[2], 'utf8')

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
    import datetime
    import re,os, sys,urllib.request
    content = urllib.request.urlopen(URL).read()
    patter = b''
    pattern = URL + ".git"
    pattern = bytes(pattern,'utf8')
    print(pattern)
    try:
        if pattern in content:

            STR1 = URL.partition("https://github.com/")
            #STR1=bytes(STR1,'utf8')
            STR2=STR1[2].partition("/")
            #STR2=bytes(STR2,'utf8')
            print (STR2[2])
            path = ROOT_DIRECTORY +"\\"+ STR2[2]
            #path=bytes(path,'utf8')
            if not os.path.exists(path):
                print (path)
                os.makedirs(path, 0o0755)
            else:
                print ("Path exists")
            print (pattern)
            pattern = pattern.decode(encoding='UTF-8')
            pattern = "\""+pattern+"\""
            cmd_string = "git clone %s %s" %(pattern, path)
            os.system(cmd_string)
        return
    except OSError as error:
        print (error)


FilterURL()
