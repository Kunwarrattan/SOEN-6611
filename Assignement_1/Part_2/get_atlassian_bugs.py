__author__ = 'kunwar'

import urllib2

FILE = open("Config.txt","r")

def Filter_File():
    STR1 = FILE.readline().partition("url = ")
    URL= STR1[2]

    STR2 = FILE.readline().partition("project_tag = ")
    PROJECT_TAG = STR2[2]

    STR3 = FILE.readline().partition("bug_start = ")
    BUG_START = STR3[2]

    STR4 = FILE.readline().partition("bug_end = ")
    BUG_END = STR4[2]

    STR5 = FILE.readline().partition("max_timeout_secs = ")
    MTS = int(STR5[2])

    STR6 = FILE.readline().partition("root_directory=")
    ROOT_DIRECTORY = STR6[2]

   # from random import randint
   # for x in range(0, 2):
    #    MTS = randint(1,MTS)
    Get_Content(URL,BUG_START,ROOT_DIRECTORY)
    return

def Get_Content(URL,BUG_Number,ROOT_DIRECTORY):
    content = urllib2.urlopen(URL).read()
    #print content
    path = ROOT_DIRECTORY +"/"+ BUG_Number

    import os
    if not os.path.exists(path):
        print path
        os.makedirs(path, 0755)
    else:
        print "Path exists"

    f = open(path+"/"+BUG_Number+".txt",'w+')
    f.write(content)
    f.read()
    f.close()

    return

Filter_File()