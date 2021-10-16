from app.log_manager import log
from datetime import date
from .model import TransactionInput


def make_transaction(transaction: TransactionInput):
    log.info(f'calling make_transaction({transaction})')

    return transaction
