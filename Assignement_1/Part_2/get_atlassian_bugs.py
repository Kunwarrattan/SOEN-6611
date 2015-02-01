__author__ = 'kunwar'

import urllib2

def getRawContent(url):
    content = urllib2.urlopen(url).read()
    #add regular expression
    return content


def writeToFile(filePath, content):
    f = open(filePath,'w')
    f.write(content) # python will convert \n to os.linesep
    f.close()
    return

def readConfig(filePath):
    lines = [line.strip() for line in open(filePath)]
    return lines[0], lines[1]


a, b = readConfig("config.txt")

print a
print b