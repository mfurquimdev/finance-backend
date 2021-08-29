from fastapi import APIRouter, HTTPException
from .controller import make_transaction
from .model import TransactionInput

from app.log_manager import log

router = APIRouter()

@router.post("/transaction",
            tags=["/transaction"],
            summary="""Endpoint to retrieve a transaction""")
def retrieve_transaction(transaction: TransactionInput):
    """ Retrieve a transaction.

        Args:
            Date (date): The date when the transaction was made

        Returns:
            Transaction: A Transaction model
    """
    log.info('POST retrieve_transaction({transaction})')

    make_transaction(transaction.date)
