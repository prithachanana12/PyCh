'''
Created on Feb 23, 2015

@author: m133293
'''

import pickle,urllib
data= pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
print data

for this in data:
    print "".join(i[0]*i[1] for i in this)
    