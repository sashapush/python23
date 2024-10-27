import requests


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property  # better idea to mark it as property. It doesn't modify anything, doesn't take any arguments or modify
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest[
            "rates"]  # we access property, since there are no () - we know we can't pass anything to said property
        to_rate = rates[to_currency]
        if from_currency == "USD":  # base is always USD
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate
