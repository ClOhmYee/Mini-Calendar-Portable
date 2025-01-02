from cryptography.fernet import Fernet
import os

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, './data/')

if not os.path.exists(data_path):
    os.makedirs(data_path)

# generate key first, get key next
if not os.path.isfile("./data/enc.key"):
    key = Fernet.generate_key()
    with open("./data/enc.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("./data/enc.key", "rb") as key_file:
        key = key_file.read()

fernet = Fernet(key)

def encryption(data_path):
    with open(data_path, "r") as data_file:
        data = data_file.read()
    
    encrypted_data = fernet.encrypt(data.encode())

    with open("./data/credentials.enc", "wb") as enc_file:
        enc_file.write(encrypted_data)

def decryption(data_path):
    with open(data_path, "rb") as data_file:
        data = data_file.read()
    
    decrypted_data = fernet.decrypt(data).decode()

    with open("./data/credentials_dec.json", "w") as dec_file:
        dec_file.write(decrypted_data)