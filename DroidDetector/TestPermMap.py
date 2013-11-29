from permissions_map import *
#Only for small testing purpose, will dele later

#{"com.android.server.WifiService": 'void enforceChangePermission()'}
#{"com.android.server.WifiService": 'android.os.Messenger getWifiServiceMessenger()'}
#{"com.android.server.WifiService": 'void disconnect()'}
#{"android.net.wifi.IWifiManager$Stub$Proxy": 'android.os.Messenger getWifiServiceMessenger()'}
#{"com.android.server.WifiService": 'void reconnect()'}
#{"com.android.server.WifiService": 'void setCountryCode(java.lang.String,boolean'}
#{"com.android.server.WifiService": 'void setFrequencyBand(int,boolean)'}
#{"com.android.server.WifiService": 'void reconnect()'}

Pa = {"com.android.server.WifiService": 'void enforceChangePermission()'}
Pb = {"com.android.server.WifiService": 'android.os.Messenger getWifiServiceMessenger()'}
Pc = {"com.android.server.WifiService": 'void disconnect()'}
Pd = {"android.net.wifi.IWifiManager$Stub$Proxy": 'android.os.Messenger getWifiServiceMessenger()'}
Pe = {"com.android.server.WifiService": 'void reconnect()'}
Pf = {"com.android.server.WifiService": 'void setCountryCode(java.lang.String,boolean'}
Pg = {"com.android.server.WifiService": 'void setFrequencyBand(int,boolean)'}
#ph =

#P1 = {"com.android.server.WifiService": 'void enforceChangePermission()'}
#P2 = {"com.android.server.WifiService": 'android.os.Messenger getWifiServiceMessenger()'}
#P3 = {"com.android.server.WifiService": 'void disconnect()'}
#P4 = {"android.net.wifi.IWifiManager$Stub$Proxy": 'android.os.Messenger getWifiServiceMessenger()'}
#P5 = {"com.android.server.WifiService": 'void reconnect()'}
#P6 = {"com.android.server.WifiService": 'void setCountryCode(java.lang.String,boolean'}
#P7 = {"com.android.server.WifiService": 'void setFrequencyBand(int,boolean)'}


#Pa = ["com.android.server.WifiService", 'void enforceChangePermission()']
#
#      #{"com.android.server.WifiService": 'android.os.Messenger getWifiServiceMessenger()'},
#      #{"com.android.server.WifiService": 'void disconnect()'},
#      #{"android.net.wifi.IWifiManager$Stub$Proxy": 'android.os.Messenger getWifiServiceMessenger()'},
#      #{"com.android.server.WifiService": 'void reconnect()'},
#      #{"com.android.server.WifiService": 'void setCountryCode(java.lang.String,boolean'},
#      #{"com.android.server.WifiService": 'void setFrequencyBand(int,boolean)'}]

print Pa