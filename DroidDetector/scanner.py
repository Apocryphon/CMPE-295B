#!/usr/bin/env python

__author__ = 'yehrc'

import sys
import os
import csv
from old_permissions_map import perm_map
from argparse import ArgumentParser
from androlyze import *
from androguard.decompiler.dad import decompile
from androguard.core.bytecodes import apk, dvm
from mapper import *


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

    #alphabet_string = string.ascii_letters
    #alphabet_list = []
    #for letter in alphabet_string:
    #    alphabet_list.append(letter)
    #
    #alphabet_list.append("d_")

    methods_list = d.get_methods()

    #for method in methods_list:
    #    if method.get_name() not in alphabet_list:
    #        print "Name: ", method.get_name()

    all_methods = dx.get_tainted_packages().get_all_methods()
    #print all_methods

    api_calls, bad_calls = compare_methods(all_methods, perms_list)
    print
    print "All of the Android API calls needing permissions: ", api_calls
    print
    print "Total API calls: ", len(all_methods)
    print "Android API calls requiring privileges: ", len(api_calls)
    print "Declared Permissions API calls: ", len(api_calls)-len(bad_calls)
    print "Undeclared Permissions API calls: ", len(bad_calls)
    print "The following are bad calls: ", bad_calls

    create_csv(len(all_methods), len(api_calls), len(bad_calls))

def create_csv(total_method_calls, total_api_calls, bad_api_calls):
    non_api_calls = total_method_calls - total_api_calls
    good_api_calls = total_api_calls - bad_api_calls

    stats_csv  = open('../HomeOne/extendbootstrap-master/stats.csv', "wb")
    writer = csv.writer(stats_csv)
    writer.writerow(["method_type", "calls"])
    writer.writerow(["Non-Android API Calls", non_api_calls])
    writer.writerow(["Declared Permissions", good_api_calls])
    writer.writerow(["Undeclared Permissions", bad_api_calls])

    stats_csv.close()



if __name__ == "__main__":
    main(sys.argv[1:])