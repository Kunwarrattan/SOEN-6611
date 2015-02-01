__author__ = 'kunwar'

import requests
from bs4 import BeautifulSoup
def start():
    FILE = open("Config.txt","r")
    STR1 = FILE.readline().partition("url=")
    URL= STR1[2]
    print URL

    from pygithub3 import Github
    gh = Github()

    s = gh.repos.list_contributors(user='poise',repo='python')

    print(s.all())

    return

start()

