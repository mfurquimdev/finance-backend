from pydantic import BaseModel
from pydantic import Field
import datetime

class TransactionInput(BaseModel):
    """ Transaction to be created to or retrieved from database """
    date: datetime.date = Field(
        datetime.date.today(),
        title="date",
        descritpion="Day of the transaction",
    )
    amount: float = Field(
        0,
        title="amount",
        descritpion="Amount paid/received in the transaction",
    )
    installments: int = Field(
        1,
        title="installments",
        descritpion="How many installments the transaction was made",
        ge=1,
    )


