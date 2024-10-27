import requests, functools


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property  # better idea to mark it as property. It doesn't modify anything, doesn't take any arguments or modify
    @functools.lru_cache(maxsize=2) #least recently used (lru), maxsize = how many pieces of data are stored. I.e caching the function.
    #since we don't have arguments - maxsize=2 is good. If we do have arguments - we should increase maxsize to account for permutations (i.e. combinations of arguments)
    #BUT there's a need to invalidate the cache, to prevent outdating the data - TO DO TTL
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
