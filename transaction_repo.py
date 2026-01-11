# Mock repository, pode ser substituído por SQLAlchemy + PostgreSQL
transactions = {}

class TransactionRepo:
    def save_transaction(self, **kwargs):
        transactions[kwargs["transaction_id"]] = kwargs
        return kwargs

    def get_transaction(self, transaction_id):
        return transactions.get(transaction_id, None)

    def update_transaction(self, tx):
        transactions[tx["transaction_id"]] = tx
        return tx
