'''
Created on Feb 22, 2015

@author: Pritha
'''

from string import maketrans
mystring="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
trans=maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print mystring.translate(trans)
    