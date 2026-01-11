from fastapi import APIRouter
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import json
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

router = APIRouter()

# chave RSA gerada em sandbox para client-side encryption (em produção integrar com KMS/HSM)
_priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
_pub = _priv.public_key()

def public_key_jwk():
    numbers = _pub.public_numbers()
    e = numbers.e.to_bytes((numbers.e.bit_length()+7)//8, 'big')
    n = numbers.n.to_bytes((numbers.n.bit_length()+7)//8, 'big')
    import base64
    def b64u(b): return base64.urlsafe_b64encode(b).rstrip(b'=').decode('ascii')
    return {
        "kty": "RSA",
        "e": b64u(e),
        "n": b64u(n),
        "alg": "RSA-OAEP-256",
        "ext": True,
        "use": "enc"
    }

@router.get("/public_key")
def get_public_key():
    return public_key_jwk()
