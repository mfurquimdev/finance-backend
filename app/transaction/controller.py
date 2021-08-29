from app.log_manager import log
from datetime import date


def make_transaction(input_date: date = date.today()):
    log.info(f'calling make_transaction({input_date})')

    return Transaction(input_date)
