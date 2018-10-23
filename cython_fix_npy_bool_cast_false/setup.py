# to build in directory, use:
#     rm -rf build && rm -f *.c && rm -f *.so && python setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

import numpy as np

extensions = [
    Extension(
        'boolFunc',
        ['boolFunc.pyx'],
        include_dirs=[np.get_include()],
    )]

setup(
    ext_modules=cythonize(extensions),
)

