__author__ = 'kunwar'


import requests
from bs4 import BeautifulSoup


#with open("Config.txt","rwu") as f:
 ##   for line in f:
  ##      print line
   ##     cleanedLine = line.strip()
    ##    if cleanedLine: # is not empty
     #       print(cleanedLine)

FILE = open("Config.txt","r")
def FilterURL():
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
    import datetime
    import re,os, sys,urllib2
    content = urllib2.urlopen(URL).read()
    pattern = URL + ".git"
    print pattern
    try:
        if pattern in content:
            STR1 = URL.partition("https://github.com/")
            STR2=STR1[2].partition("/")
            print STR2[2]
            path = ROOT_DIRECTORY +"/"+ STR2[2]
            if not os.path.exists(path):
                print path
                os.makedirs(path, 0755)
            else:
                print "Path exists"
            print pattern
            cmd_string = "git clone %s %s" %(pattern, path)
            os.system(cmd_string)
        return
    except OSError as error:
        print error


FilterURL()