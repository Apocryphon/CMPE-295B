__author__ = 'doiiiob'

Pa = {"com.android.server.WifiService": 'void enforceChangePermission()'}
Pb = {"com.android.server.WifiService": 'android.os.Messenger getWifiServiceMessenger()'}
Pc = {"com.android.server.WifiService": 'void disconnect()'}
Pd = {"android.net.wifi.IWifiManager$Stub$Proxy": 'android.os.Messenger getWifiServiceMessenger()'}
Pe = {"com.android.server.WifiService": 'void reconnect()'}
Pf = {"com.android.server.WifiService": 'void setCountryCode(java.lang.String,boolean'}
Pg = {"com.android.server.WifiService": 'void setFrequencyBand(int,boolean)'}

Ptest = {"com.android.server.WifiService": 'void reconnect()'}
Ptest2 = {"com.android.server.WifiService": 'void setFrequencyBand(int,boolean)'}

master_p= []
master_p.append(Ptest)
master_p.append(Ptest2)

#for i in xrange(0, len(master_p)):
#    match_dict = {k:v for k,v in master_p[i].items()
#                if any(k in dicts for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))
#            and any(dicts.get(k)==v for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))}
#    print match_dict

list = []
for i in xrange(0, len(master_p)):
    match_dict = {k:v for k,v in master_p[i].items()
                if any(k in dicts for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))
            and any(dicts.get(k)==v for dicts in (Pa,Pb,Pc,Pd,Pe,Pf,Pg))}
    list.append(match_dict)

print list
