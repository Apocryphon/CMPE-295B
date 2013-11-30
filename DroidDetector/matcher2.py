#!/usr/bin/env python

__author__ = 'yehrc'

import sys
import datetime
from permissions_map2 import perm_map2

Ptest = {"com.android.server.WifiService": 'void reconnect()'}
Ptest2 = {"com.android.server.WifiService": 'void setFrequencyBand(int,boolean)'}
Ptest3 = {"com.rebelvox.voxer.c.a": 'java.util.concurrent.ConcurrentHashMap f()'}

#master_p= []
#master_p.append(Ptest)
#master_p.append(Ptest2)
#master_p.append(Ptest3)



#for i in xrange(0, len(master_p)):
#    match_dict = {k:v for k,v in master_p[i].items()
#                if any(k in dicts for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))
#            and any(dicts.get(k)==v for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))}
#    print match_dict



#for i in xrange(0, len(master_p)):
#    match_dict = {k:v for k,v in master_p[i].items()
#                if any(k in dicts for dicts in Plist)
#            and any(dicts.get(k)==v for dicts in Plist)}
#    list.append(match_dict)

# ignore call_count for now, this was to count how many API calls total are in the permission map
#call_count = 0
#for perm in perm_map2:
#    #print perm
#    for plist in perm_map2[perm]:
#        #print plist
#        call_count += len(plist)
#print call_count

def compare_methods(master_p):
    print "starting time: ", datetime.datetime.now()


    list = []
    for i in xrange(0, len(master_p)):              # master_p only contains two dictionaries, 0 to 2
        for perm in perm_map2.iterkeys():           # perm refers to the permission name, which are the keys in the dict
            #print "perm is: ", perm
            for call_dict in perm_map2[perm]:       # dict of API call e.g. {'com.android.server.WifiService': 'void stopWifi()'}
                #print "dictionary is: ", call_dict
                for k,v in master_p[i].items():     # for all of the key-value pairs in the dictionaries we're looking for
                    #print "k: %s, v: %s" % (k, v)
                    match_dict = {k:v for k,v in master_p[i].items()
                        if any(k in keys for keys in call_dict.iterkeys())
                        and any(call_dict[keys] == v for keys in call_dict.iterkeys())}
                    if match_dict and match_dict not in list:   # check to see if match_dict is NOT blank, i.e. { }, { } or already present
                        list.append(match_dict)
    print "ending time: ", datetime.datetime.now()

    return list
