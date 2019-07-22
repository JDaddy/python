#!/usr/bin/env python3

#ipchk = '192.168.0.0'
ipchk = input('Apply an IP Address: ')

if ipchk == '192.168.70.1' :
    print('Looks like the IP address was set: ' + ipchk + ' This is not recommended')
elif ipchk:
    print('wow, you so cool' + ipchk + ' is set!')
else:
    print('Super genios')

