#!/usr/bin/python
#

import re

f = open ('/var/log/dirsrv/slapd-ldapm01/access', 'r');

ip = {}

for l in f.readlines():
    m = re.search(r"connection from (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) to", l)

    if m:
        l = l.replace("\n", "")
        ip[m.group(1)] = "1"

for key in ip.keys():
    print key
            
