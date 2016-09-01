#!/usr/bin/python3

import sys
args = sys.argv
srv = 'ch4l.co.uk'
pth = '/myip/get.php'
if len(args) > 1:
    srv = args[1]
if len(args) > 2:
    pth = args[2]

import http.client
conn = http.client.HTTPConnection(srv)
conn.request("GET",pth)
response = conn.getresponse()
if response.status == 200:
    print(response.read().decode())
else:
    print(response.status,response.reason)
conn.close()
