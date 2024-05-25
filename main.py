import sys
from encryption import encrypt_folder
from decryption import decrypt_folder

def main():
    path = sys.argv[2]
    if sys.argv[1] == "encrypt": 
        print("KEY:",encrypt_folder(path))

    elif sys.argv[1] == "decrypt":
        storing_key = input("Key: ").encode()
        decrypt_folder(path, storing_key)
            
if __name__ == "__main__":
    main()
