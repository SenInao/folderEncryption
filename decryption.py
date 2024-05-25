from cryptography.fernet import Fernet
import os
from base64 import b64decode
from utils import getfolders, read_file

def decrypt(content, key):
    return key.decrypt(content)

def decrypt_folder(path, storing_key):
    key = Fernet(storing_key)
    folders, files = getfolders(path)

    if folders:
        for folder in folders:
            folder_list = folder.split("\\")
            f = ""
            for item in folder_list:
                new = b64decode(item.encode()).decode()
                f = os.path.join(f, new)
            os.makedirs("decrypted_"+f)
    else:
        new = b64decode(path.encode()).decode()
        f = os.path.join("", new)
        os.makedirs("decrypted_"+f)
    
    for file in files:
        content = read_file(file)
        decrypted = decrypt(content, key)
        file_list = file.split("\\")
        f = ""
        for item in file_list:
            new = b64decode(item.encode()).decode()
            f = os.path.join(f, new)

        with open("decrypted_"+f, "wb") as f:
            f.write(decrypted)
            print(f'Done decrypting "{f}"')
