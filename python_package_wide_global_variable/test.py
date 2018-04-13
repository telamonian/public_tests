#!/usr/bin/env python2
import argparse
import sys

from test_utils.py import summation, flags

debug_flag = {'setting' : False}

def main():
    args = get_args()
    flags.debug = args['debug']
    print summation(5, 6, 7)

def get_args():
    parser = argparse.ArgumentParser(description='Test program')
    parser.add_argument('-d','--debug', action='store_true', help='Debug True/False', default=False)
    args = vars(parser.parse_args())
    return args

if __name__=='__main__':
    main()
