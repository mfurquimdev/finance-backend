from fastapi import APIRouter, HTTPException
from .controller import make_transaction
from .model import TransactionInput

from app.log_manager import log

router = APIRouter()

@router.get("/",
            tags=["/"],
            summary="""Endpoint to say hello""")
def hello_world():
    """ Say hellor

        Args:
            None

        Returns:
            str: 'Hello World!'
    """
    log.info('GET hello_world()')

    return 'Hello World!'

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
    log.info(f'POST retrieve_transaction({transaction})')

    made_transaction = make_transaction(make_transaction(transaction.transaction_date))
    log.info(f'Return of make_transaction -> {made_transaction}')

    return made_transaction
