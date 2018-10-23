import numpy as np
cimport numpy as np

__all__ = ['boolFunc', 'boolFuncCast',
           'intFunc', 'intFuncCast']

def boolFunc(np.ndarray[np.npy_bool, ndim=1] npdata):
    return npdata

def boolFuncCast(np.ndarray[np.npy_bool, ndim=1, cast=True] npdata):
    return npdata

def intFunc(np.ndarray[np.npy_long, ndim=1] npdata):
    return npdata

def intFuncCast(np.ndarray[np.npy_long, ndim=1, cast=True] npdata):
    return npdata

