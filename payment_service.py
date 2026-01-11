import uuid
from datetime import datetime, timedelta
from app.repositories.transaction_repo import TransactionRepo
from app.kms_wrapper import KMSWrapper
from app.utils.qr_generator import generate_qr_code
from app.utils.link_generator import generate_payment_link

class PaymentService:
    def __init__(self):
        self.repo = TransactionRepo()
        self.kms = KMSWrapper()

    def create_payment(self, amount: float, method: str, card_data: dict = None):
        # Tokenização de cartão
        token = None
        if card_data:
            token = self.kms.encrypt_card(card_data)

        transaction_id = str(uuid.uuid4())
        payment_link = generate_payment_link(transaction_id)
        qr_code = generate_qr_code(payment_link)

        transaction = self.repo.save_transaction(
            transaction_id=transaction_id,
            amount=amount,
            method=method,
            token=token,
            status="pending",
            created_at=datetime.utcnow()
        )
        return {
            "transaction_id": transaction_id,
            "payment_link": payment_link,
            "qr_code": qr_code
        }

    def capture_payment(self, transaction_id: str):
        tx = self.repo.get_transaction(transaction_id)
        tx["status"] = "captured"
        self.repo.update_transaction(tx)
        return tx

    def refund_payment(self, transaction_id: str):
        tx = self.repo.get_transaction(transaction_id)
        tx["status"] = "refunded"
        self.repo.update_transaction(tx)
        return tx
