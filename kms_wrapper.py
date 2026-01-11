from cryptography.fernet import Fernet
import os

class KMSWrapper:
    """
    Abstração para integração com AWS/GCP/Azure KMS.
    Aqui usamos Fernet para sandbox/teste.
    """

    def __init__(self):
        key = os.environ.get("KMS_KEY")
        if not key:
            key = Fernet.generate_key().decode()
            os.environ["KMS_KEY"] = key
        self.cipher = Fernet(key.encode())

    def encrypt_card(self, card_data: dict) -> str:
        import json
        plaintext = json.dumps(card_data).encode()
        return self.cipher.encrypt(plaintext).decode()

    def decrypt_card(self, token: str) -> dict:
        import json
        decrypted = self.cipher.decrypt(token.encode())
        return json.loads(decrypted)
