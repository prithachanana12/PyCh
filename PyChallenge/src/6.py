'''
Created on Feb 25, 2015

@author: m133293
'''

##extracting the zipfile from webpage - one time operation
'''
import requests as r,zipfile as z,StringIO as s
data=r.get("http://www.pythonchallenge.com/pc/def/channel.zip")
#print data.ok
#print data.encoding
nothings=z.ZipFile(s.StringIO(data.content))
nothings.extractall("H:/PyCh-git/PyChallenge/src/channel_zip")
'''
flag=True
##import os
def readfiles(infile):
    ##a chunk of code to read files and go to next file if it has a\
    ##number else, print the lines of the file
    inData=infile.readline()
    if any(char.isdigit() for char in inData):
        ans=inData.split(' ')[-1]
    else:
        ans=inData
    return ans

##prints the start instructions from readme
with open("H:/PyCh-git/PyChallenge/src/channel_zip/readme.txt","r") as first:
    print first.readlines()

##n=len([name for name in os.listdir("H:/PyCh-git/PyChallenge/src/channel_zip") if os.path.isfile(name)])

##std input for the first file to read
fname=raw_input("Initial file to read:")
with open("H:/PyCh-git/PyChallenge/src/channel_zip/%s.txt" %fname,"r") as f1:
    succ=readfiles(f1)

while flag:
    if succ.isdigit():
        print succ
        with open("H:/PyCh-git/PyChallenge/src/channel_zip/%s.txt" %succ,"r") as f2:
            succ=readfiles(f2)
    else:
        print succ
        flag=False
        
        
    
    

