#!/usr/bin/env python

__author__ = 'yehrc'

import sys
import datetime
import re
from permissions_map import perm_map

# ignore call_count for now, this was to count how many API calls total are in the permission map
#call_count = 0
#for perm in perm_map2:
#    #print perm
#    for plist in perm_map2[perm]:
#        #print plist
#        call_count += len(plist)
#print call_count

def compare_methods(all_method_calls_list, declared_perms_list):
    print "starting time: ", datetime.datetime.now()
    print

    undeclared_permissions = {}
    api_calls_list = []

    for i in xrange(0, len(all_method_calls_list)):
        for perm in perm_map.iterkeys():                # perm refers to the permission name, which are the keys in the dict
            #print "perm is: ", perm
            for call_dict in perm_map[perm]:            # dict of API call e.g. {'com.android.server.WifiService': 'void stopWifi()'}
                #print "dictionary is: ", call_dict
                #for k,v in all_method_calls_list[i].items():         # for all of the key-value pairs in the dictionaries we're looking for
                #    #print "k: %s, v: %s" % (k, v)
                match_dict = {k:v for k,v in all_method_calls_list[i].items()
                    if any(k in keys for keys in call_dict)
                    and any(call_dict[keys] == v for keys in call_dict)}
                if match_dict and match_dict not in api_calls_list:   # check to see if match_dict is NOT blank, i.e. {{ }, { }} or already present
                    api_calls_list.append(match_dict)
                    call_perm = re.findall(".*permission.(.*)", perm)[0]
                    print match_dict, " used permission: ", call_perm
                    if call_perm not in declared_perms_list:
                        print "Use of undeclared permission found: ", match_dict
                        print "Missing permission: ", call_perm
                        if call_perm not in undeclared_permissions:
                            undeclared_permissions[call_perm] = []
                            undeclared_permissions[call_perm].append(match_dict)
                        else:
                            undeclared_permissions[call_perm].append(call_perm)

    print
    print "ending time: ", datetime.datetime.now()
    print

    return api_calls_list, undeclared_permissions
