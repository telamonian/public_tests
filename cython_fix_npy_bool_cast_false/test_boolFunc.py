#!/usr/bin/env python
from boolFunc import boolFunc
import numpy as np

# generate random boolArr
arr = np.random.randint(0,2, size=3, dtype=int)
boolArr = np.array(arr, dtype=bool)

# test cython function
boolFunc(boolArr)

