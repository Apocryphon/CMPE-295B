__author__ = 'yehrc'

import sys
import os
from argparse import ArgumentParser
from androlyze import *
from androguard.decompiler.dad import decompile
from androguard.core.bytecodes import apk, dvm

def main(argv):
    parser = ArgumentParser()
    parser.add_argument("-a", "--apk", dest="apk",
                        help="apk FILE", metavar="FILE")
    args = parser.parse_args()
    apk_file = args.apk
    a, d, dx = AnalyzeAPK(apk_file, decompiler="DAD")
    show_Permissions(dx)



if __name__ == "__main__":
    main(sys.argv[1:])