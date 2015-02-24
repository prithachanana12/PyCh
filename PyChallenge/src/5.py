'''
Created on Feb 23, 2015

@author: m133293
'''

import pickle,urllib
data= pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
print data