from pydantic import BaseModel
from typing import Optional, Dict

class PaymentCreateRequest(BaseModel):
    amount: float
    method: str
    card_data: Optional[Dict] = None
