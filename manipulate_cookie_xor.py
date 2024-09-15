#!/usr/bin/env python3

"""
This script is designed for an OverTheWire CTF challenge. It involves manipulating cookies and using XOR encryption/decryption 
to reveal a hidden password.

The challenge presents a color input field and checks if the `showpassword` attribute is set to "yes". The script performs the 
following steps:
1. Extracts the encrypted cookie value.
2. Decrypts the cookie value using XOR with a known plaintext.
3. Uses the decrypted value to set up a new cookie with `showpassword` set to "yes".
4. Sends a request to the server with the new cookie to reveal the password.

"""

import requests
import json
import base64
import urllib.parse

url='http://natas11.natas.labs.overthewire.org/?bgcolor=%23ffffff'


username='natas11'
password='UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk'

cookie_value='HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg='
cookie={
	'data':'HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc='
}


ciphertext = b"HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg="
ciphertext = base64.decodebytes(ciphertext)
plaintext = {"showpassword":"no", "bgcolor":"#ffffff"}
# Here, we remove the space as JSON implementation in Python is different from PHP
plaintext = json.dumps(plaintext).encode('utf-8').replace(b" ", b"")
def xor_decrypt(plaintext, ciphertext):
    secret = ""
    for x in range(len(plaintext)):
        secret += str(chr(ciphertext[x] ^ plaintext[x % len(plaintext)]))

    return secret

secret = xor_decrypt(ciphertext, plaintext)
print(secret)


key = b"eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeD"
new_cookie = {"showpassword":"yes", "bgcolor":"#ffffff"}
new_cookie = json.dumps(new_cookie).encode('utf-8').replace(b" ", b"")

def xor_encrypt(key, cookie):
    data = ""
    for x in range(len(key)):
        data += str(chr(cookie[x] ^ key[x % len(key)]))

    data = base64.encodebytes(data.encode('utf-8'))
    return data

data = xor_encrypt(key, new_cookie)
print(data)

r=requests.get(url,auth=(username,password),cookies=cookie)
print(r.text)