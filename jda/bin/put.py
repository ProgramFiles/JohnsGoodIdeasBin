#!/usr/bin/python3

import sys
args = sys.argv
srv = 'ch4l.co.uk'
pth = '/myip/put.php'
if len(args) > 1:
    srv = args[1]
if len(args) > 2:
    pth = args[2]

import http.client, urllib.parse
params = urllib.parse.urlencode({'turnickle':'mrflibble'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = http.client.HTTPConnection(srv)
conn.request("POST",pth,params,headers)
response = conn.getresponse()
if response.status == 200:
    print(response.read().decode())
else:
    print(response.status,response.reason)
conn.close()
