from cryptography.fernet import Fernet
import os
from base64 import b64encode
from utils import getfolders, read_file

def generate_key():
    key = Fernet.generate_key()
    return Fernet(key), key

def encrypt(content, key):
    return key.encrypt(content)

def encrypt_folder(path):
    folders, files = getfolders(path)
    key, storing_key = generate_key()

    if folders:
        for folder in folders:
            folder_list = folder.split("\\")
            f = ""
            for item in folder_list:
                new = b64encode(item.encode())
                f = os.path.join(f, new.decode())
            os.makedirs(f)
    else:
        new = b64encode(path.encode())
        os.mkdir(new)
    
    for file in files:
        content = read_file(file)
        encrypted = encrypt(content, key)
        file_list = file.split("\\")

        fi =""
        for item in file_list:
            new = b64encode(item.encode())
            fi = os.path.join(fi, new.decode())
            
        with open(fi, "wb") as f:
            f.write(encrypted)
            print(f'Done encrypting "{file}"')

    return storing_key.decode()
