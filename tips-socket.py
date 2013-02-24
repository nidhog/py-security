#!/usr/bin/env python
#---coding:utf8---
#author offensive

import sys
import socket



socket.setdefaulttimeout(6)
s = socket.socket()
s.connect(("www.php.net",22))
header = s.recv(1024)
print "[+]"+header
