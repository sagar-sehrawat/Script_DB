#!/usr/bin/env python3

from Cryptodome.Cipher import AES
import hashlib
import binascii
import requests

cipher=requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ciphertext_hex=cipher.json()['ciphertext']

with open('words','r') as w:
	for word in w:
		word=word.strip()
		attempt_key=hashlib.md5(word.encode()).hexdigest()
		# print(attempt_key)

		cipher_text=bytes.fromhex(ciphertext_hex)
		key=bytes.fromhex(attempt_key)
		cipher=AES.new(key,AES.MODE_ECB)
		try:
			decrypt=cipher.decrypt(cipher_text)
			result=binascii.unhexlify(decrypt.hex())
			if result.startswith('crypt'.encode()):
				print("key is %s" % word)
				print(result.decode('utf-8'))
				break
		except ValueError as e:
			continue
