'''
Created on Feb 23, 2015

@author: m133293
'''
####expect results in ~250 iterations instead of 400 mentioned
import urllib
nothing=12345
for i in range(1,401):
    gh=urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(nothing)).read()
    if any(char.isdigit() for char in gh):
        nothing=gh.split(' ')[-1]
    else:
        print gh
        print nothing
        break

nothing=int(nothing)/2
for j in range(i,401):
    gh=urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(nothing)).read()
    if any(char.isdigit() for char in gh):
        nothing=gh.split(' ')[-1]
    else:
        print gh
        print nothing
        print j
        break
