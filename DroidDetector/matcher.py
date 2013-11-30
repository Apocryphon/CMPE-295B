#!/usr/bin/env python

__author__ = 'doiiiob'

from old_permissions_map import *
from scanner import *
from TestPermMap import *
import copy
import json
#Pa = {"com.android.server.WifiService": 'void enforceChangePermission()'}
#Pb = {"com.android.server.WifiService": 'android.os.Messenger getWifiServiceMessenger()'}
#Pc = {"com.android.server.WifiService": 'void disconnect()'}
#Pd = {"android.net.wifi.IWifiManager$Stub$Proxy": 'android.os.Messenger getWifiServiceMessenger()'}
#Pe = {"com.android.server.WifiService": 'void reconnect()'}
#Pf = {"com.android.server.WifiService": 'void setCountryCode(java.lang.String,boolean'}
#Pg = {"com.android.server.WifiService": 'void setFrequencyBand(int,boolean)'}

Ptest = {"com.android.server.WifiService": 'void enforceChangePermission()'}
Ptest2 = {"com.android.server.WifiService": 'android.os.Messenger getWifiServiceMessenger()'}

pList = []
#pList.append(Pa)                                        #way1
#pList.append(Pb)
#pList.append(Pc)
#pList.append(Pd)
#pList.append(Pe)
#pList.append(Pf)
#pList.append(Pg)

#print pList
pList.extend((Pa, Pb, Pc, Pd, Pe, Pf, Pg))             #way2: another way, but still not good
#print type(pList)
#print pList

master_p= []
master_p.extend((Ptest, Ptest2))
#
#print type(master_p)
#print master_p

#from itertools import izip
#i = iter(master_p)
#master_pMap = dict(izip(i, i))


#for i in xrange(0, len(master_p)):
#    match_dict = {k:v for k,v in master_p[i].items()
#                if any(k in dicts for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))
#            and any(dicts.get(k)==v for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))}
#    print match_dict

#dictmap = {}
#dictmap


list = []
for i in xrange(0, len(master_p)):
    match_dict = {k:v for k,v in master_p[i].items()
                if any(k in dicts for dicts in pList)
            and any(dicts.get(k)==v for dicts in pList)}
    list.append(match_dict)

print "The result: ", list




#Don't change this part! The original alg
#
#master_p= []
#master_p.append(Ptest)
#master_p.append(Ptest2)

#list = []
#for i in xrange(0, len(master_p)):
#    match_dict = {k:v for k,v in master_p[i].items()
#                if any(k in dicts for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))
#            and any(dicts.get(k)==v for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))}
#    list.append(match_dict)
#
#print list