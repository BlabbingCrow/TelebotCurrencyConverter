from pycbrf import ExchangeRates
from datetime import datetime


def get_currency_cost(currency_code):
    rates = ExchangeRates(datetime.today())
    for rate in rates.rates:
        if rate.code == currency_code:
            return rates[currency_code].value
    return None

