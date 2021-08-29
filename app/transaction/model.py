from pydantic import BaseModel
from pydantic import Field
from datetime import date

class TransactionInput(BaseModel):
    """ Transaction to be created to or retrieved from database """
    transaction_date: date = Field(
        None,
        title="date",
        descritpion="Day of the transaction",
    )

