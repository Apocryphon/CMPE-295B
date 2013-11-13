#!/usr/bin/env python

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

    perms_list = dx.get_permissions( [] ).keys()
    perms_list.sort()
    print "Permissions requested by app are: ", perms_list

    alphabet_list = string.ascii_letters

    #alphabet_list = []
    #alphabet_list.append(string.uppercase)
    #alphabet_list.append(string.lowercase)
    #print alphabet_list

    methods_list = d.get_methods()
    for method in methods_list:
        if method.get_name() not in alphabet_list:
            print "Name: ", method.get_name()
            #print method.show_info()


if __name__ == "__main__":
    main(sys.argv[1:])