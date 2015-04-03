__author__ = 'kunwar'

import urllib.request,time

FILE = open("Config.txt","r")

def Filter_File():
    STR1 = FILE.readline().partition("url = ")
    URL= STR1[2].strip()

    STR2 = FILE.readline().partition("project_tag = ")
    PROJECT_TAG = STR2[2].strip()

    STR3 = FILE.readline().partition("bug_start = ")
    BUG_START = STR3[2]

    STR4 = FILE.readline().partition("bug_end = ")
    BUG_END = STR4[2]

    STR5 = FILE.readline().partition("max_timeout_secs = ")
    MTS = int(STR5[2])

    STR6 = FILE.readline().partition("root_directory=")
    ROOT_DIRECTORY = STR6[2]

    BUG_NUMBER = int(BUG_START)

    from random import randint
    for x in range(int(BUG_START), int(BUG_END)):
        MTS = randint(1,MTS)
        time.sleep(MTS)
        string_url = "https://"+URL+".atlassian.net"+"/browse/"+PROJECT_TAG+"-"+str(BUG_NUMBER)+"?jql="
        print (string_url)
        Get_Content(string_url,BUG_NUMBER,ROOT_DIRECTORY)
        BUG_NUMBER = BUG_NUMBER+1
    return

def Get_Content(URL,BUG_Number,ROOT_DIRECTORY):

    content = urllib.request.urlopen(URL).read()

    path = ROOT_DIRECTORY +"/"+ str(BUG_Number)

    import os
    if not os.path.exists(path):
        print (path)
        os.makedirs(path, 0o0755)
    else:
        print ("Path exists")

    f = open(path+"/"+str(BUG_Number)+".txt",'w+')
    content = content.decode(encoding='UTF-8')
    f.write(content)
    f.read()
    f.close()

    return

Filter_File()
