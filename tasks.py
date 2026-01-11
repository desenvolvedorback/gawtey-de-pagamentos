from .celery_app import celery
from .repositories.transaction_repo import TransactionRepo
from .utils.email_service import send_email
import time

repo = TransactionRepo()

@celery.task(bind=True, name="app.tasks.process_settlement")
def process_settlement(self, transaction_id):
    # Simula processamento demorado (conciliacao / acquirer)
    tx = repo.get_transaction(transaction_id)
    if not tx:
        return {"status":"not_found"}
    time.sleep(1)  # simulacao
    tx["status"] = "settled"
    repo.update_transaction(tx)
    # enviar email de confirmação (mock)
    send_email("customer@example.com", "Pagamento confirmado", f"Transação {transaction_id} confirmada.")
    return {"status":"settled","transaction_id":transaction_id}
