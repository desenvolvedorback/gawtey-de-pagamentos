from fastapi import APIRouter, HTTPException
from app.services.payment_service import PaymentService
from app.schemas.payment_schemas import PaymentCreateRequest

router = APIRouter()
service = PaymentService()

@router.post("/create")
def create_payment(request: PaymentCreateRequest):
    try:
        result = service.create_payment(
            amount=request.amount,
            method=request.method,
            card_data=request.card_data
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/capture/{transaction_id}")
def capture_payment(transaction_id: str):
    return service.capture_payment(transaction_id)

@router.post("/refund/{transaction_id}")
def refund_payment(transaction_id: str):
    return service.refund_payment(transaction_id)
