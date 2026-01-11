import pytest
from fastapi.testclient import TestClient
from app.main import app
import concurrent.futures

client = TestClient(app)

def create_payment(i):
    payload = {
        "amount": 100.0 + i,
        "method": "card",
        "card_data": {"number":"4111111111111111","expiry":"12/25","cvv":"123","name":"Teste"}
    }
    res = client.post("/api/payments/create", json=payload)
    return res.status_code

def test_concurrent_requests():
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(create_payment, i) for i in range(1000)]
        results = [f.result() for f in futures]
    assert all(r == 200 for r in results)
