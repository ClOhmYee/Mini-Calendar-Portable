from cryptography.fernet import Fernet
import os

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, "data")
token_path = os.path.join(data_path, "token.json")
key_path = os.path.join(data_path, "enc.key")
enc_data_path = os.path.join(data_path, "token_enc.json")

if not os.path.exists(data_path):
    os.makedirs(data_path)

# generate key first, get key next
if not os.path.isfile(key_path):
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
else:
    with open(key_path, "rb") as key_file:
        key = key_file.read()

fernet = Fernet(key)

def encryption(input_path):
    with open(input_path, "r") as data_file:
        data = data_file.read()
    
    encrypted_data = fernet.encrypt(data.encode())

    with open(enc_data_path, "wb") as enc_file:
        enc_file.write(encrypted_data)

def decryption(input_path):
    with open(input_path, "rb") as data_file:
        data = data_file.read()
    
    decrypted_data = fernet.decrypt(data).decode()

    dec_data_path = os.path.join(data_path, "token.json")

    with open(dec_data_path, "w") as dec_file:
        dec_file.write(decrypted_data)