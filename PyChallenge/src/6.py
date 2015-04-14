'''
Created on Feb 25, 2015

@author: m133293
'''

import requests as r,zipfile as z,StringIO as s
flag=True
finalPic=[]

##extracting the zipfile from webpage
data=r.get("http://www.pythonchallenge.com/pc/def/channel.zip")
#print data.ok
nothings=z.ZipFile(s.StringIO(data.content))
##nothings.extractall("H:/PyCh-git/PyChallenge/src/channel_zip") 

###function to loop through files of the archive based on the 'nothing' value
def readfiles(infile):
    inData=infile.readline()
    if any(char.isdigit() for char in inData):
        ans=inData.split(' ')[-1]
    else:
        ans=inData
    return ans

##prints the start instructions from readme
######### with open("H:/PyCh-git/PyChallenge/src/channel_zip/readme.txt","r") as first:
#########     print first.readlines()
with nothings.open("readme.txt","r") as first:
    print first.readlines()

##std input for the first file to read
fname=raw_input("Initial file to read:")
with nothings.open("%s.txt" %fname,"r") as f1:
    succ=readfiles(f1)

while flag:
    if succ.isdigit():
        #print succ
        with nothings.open("%s.txt" %succ,"r") as f2:
            succ=readfiles(f2)
    else:
        #print succ
        flag=False

print "".join(finalPic)
        
    
    

