import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_payment():
    payload = {
        "amount": 100.0,
        "method": "card",
        "card_data": {"number":"4111111111111111","expiry":"12/25","cvv":"123","name":"Teste"}
    }
    res = client.post("/api/payments/create", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "transaction_id" in data
    assert "payment_link" in data
    assert "qr_code" in data
