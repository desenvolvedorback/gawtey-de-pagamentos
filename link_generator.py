import uuid
from datetime import datetime, timedelta

def generate_payment_link(transaction_id: str) -> str:
    token = uuid.uuid4()
    expiry = (datetime.utcnow() + timedelta(hours=1)).isoformat()
    return f"http://localhost:8000/pay/{transaction_id}?token={token}&exp={expiry}"
