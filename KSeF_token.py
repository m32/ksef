from base64 import b64encode
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_KSeF_token(auth_token, challenge_timestamp, pemdata):
    
    token = auth_token + "|" + challenge_timestamp
    token = str.encode(token)
    public_key = serialization.load_pem_public_key(pemdata.encode())
    x = public_key.encrypt(
        token,
        padding.PKCS1v15()
    )
    x = b64encode(x)
    return x 
