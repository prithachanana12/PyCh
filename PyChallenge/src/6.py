'''
Created on Feb 25, 2015

@author: m133293
'''

# import requests as r,zipfile as z,StringIO as s
# data=r.get("http://www.pythonchallenge.com/pc/def/channel.zip")
# #print data.ok
# #print data.encoding
# nothings=z.ZipFile(s.StringIO(data.content))
# nothings.extractall("H:/PyCh-git/PyChallenge/src/channel_zip")

with open("H:/PyCh-git/PyChallenge/src/channel_zip/readme.txt","r") as first:
    print first.readlines()

s=raw_input("Where should I start from?")
with open()