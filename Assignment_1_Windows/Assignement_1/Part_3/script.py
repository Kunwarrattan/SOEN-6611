__author__ = 'kunwar'

import requests
from bs4 import BeautifulSoup

def start():
    FILE = open("../Part_1/Config.txt","r")
    STR1 = FILE.readline().partition("url=")
    URL= STR1[2]

    STR2 = FILE.readline().partition("root_directory=")
    ROOT = STR2[2]

    print (ROOT)

    import os
    path = ROOT+"/"+"Contributors"
    if not os.path.exists(path):
        print (path)
        os.makedirs(path, 0o0755)
    else:
        print ("Path exists")

    f = open(path+"/"+"author"+".txt",'w+')

    from pygithub3 import Github
    gh = Github()
    s = gh.repos.list_contributors(user='poise',repo='python')
    for page in s:
        for results in page:
          string = str(results)
          print (results)
          print ("------")
          f.write(string)
          f.write("\n")
    #print(s.all())
    return

    f.read()
    f.close()

start()

