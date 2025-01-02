import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)

from src import encryption as enc

credentials_path = os.path.join(project_root, 'data/credentials.json')

# encryption test
if os.path.isfile(credentials_path):
    enc.encryption(credentials_path)
    print("encryption complete")
else:
    print("error finding credentials.json")

# decryption test (using previous result)
enc_credentials_path = os.path.join(project_root, 'data/credentials.enc')
if os.path.isfile(credentials_path):
    enc.decryption(enc_credentials_path)
    print("decryption complete")
else:
    print("error finding credentials.enc")