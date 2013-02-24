#!/usr/bin/env python
#-----coding:utf8------
import os
import sys
import base64
import math

def test(txt,key,operation='ENCODE'):
	if operation == 'ENCODE':
		txt = str(txt)
	else:
		txt = base64.decodestring(str(txt))

	length = len(key)
	code = ''
	for i in range(length):
		k = i%length
		code += chr(ord(txt[i])^int(key[k]))
	if  operation == 'ENCODE':
		code = base64.encodestring(code)
	return code
def main():
	print 'helloworld'
	print test("heloworld",'1232131','ENCODE')

if __name__ == '__main__':
	main()
