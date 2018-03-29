#!/usr/bin/env python3
from collections import OrderedDict
import math
import numpy as np

def getComps():
    return [
        OrderedDict([
            ('(8885558**0.5)**2',     (8885558**0.5)**2),
            ('math.sqrt(8885558)**2', math.sqrt(8885558)**2),
        ]),
        OrderedDict([
            ('2**1023.99999999999',                 2**1023.99999999999),
            ('(math.sqrt(2**1023.99999999999))**2', (math.sqrt(2**1023.99999999999))**2),
            ('((2**1023.99999999999)**0.5)**2',     ((2**1023.99999999999)**0.5)**2),
        ]),
        OrderedDict([
            ('((2**1023.99999999999)**0.5)**2 - 2**1023.99999999999',     ((2**1023.99999999999)**0.5)**2 - 2**1023.99999999999),
            ('(math.sqrt(2**1023.99999999999))**2 - 2**1023.99999999999', (math.sqrt(2**1023.99999999999))**2 - 2**1023.99999999999),
        ]),
    ]

def getResiduals():
    return OrderedDict([
        (' - '.join(kpair), np.diff(vpair)[0])
        for d in getComps()
        for kpair,vpair in zip(zip(list(d.keys())[:-1], list(d.keys())[1:]), zip(list(d.values())[:-1], list(d.values())[1:]))
    ])

def printComps():
    for comp in getComps():
        keylen = np.max([len(key) for key in comp.keys()])
        for key,val in comp.items():
            print(('%%%ds: ' % keylen) % key, end='')
            print(val)
        print()

def printResiduals():
    for key,val in getResiduals().items():
        print(key, val, sep=': ')

if __name__=='__main__':
    print('Comparison of results of various methods:\n')
    printComps()

    print('Residual differences between results of various methods:\n')
    printResiduals()
