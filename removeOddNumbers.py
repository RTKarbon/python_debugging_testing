#!/usr/bin/env python

# This verion has runtime error!
def removeOddNumbersV1(l):
    for i in range(len(l)):
        if l[i] % 2 != 0:
            del l[i]
    return l

# This version has a bug!
def removeOddNumbersV2(l):
    for n in l:
        if n % 2 != 0:
            l.remove(n)
    return l
 
# This is correct verion
def removeOddNumbersV3(l):
    return [v for v in l if v % 2 == 0]

