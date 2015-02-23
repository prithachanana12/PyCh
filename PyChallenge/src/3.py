'''
Created on Feb 23, 2015

@author: m133293
'''

import re
with open("3.txt","r") as infile:
    data=infile.read().replace('\n','')
mymatch=re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',data)
m=[x[4:-4] for x in mymatch]
print ''.join(m)

    