'''
Created on Feb 22, 2015

@author: Pritha
'''
import re
with open("rare.txt","r") as infile:
    data=infile.read().replace("\n","")
mymatches=re.findall('[a-zA-Z]',data)
print ''.join(mymatches)


