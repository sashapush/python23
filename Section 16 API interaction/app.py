import requests
from libs.openexchange import OpenExchangeClient

APP_ID = "0bf24b2a822d4e47b1482e7ff53db7d2"

client = OpenExchangeClient(APP_ID)

usd_amount = int(input("Type dollars here: "))
gbp_amount = client.convert(usd_amount, "USD", "GBP")
print(f"{usd_amount} USD is {gbp_amount:.2f} GBP") #:.2f - 2 decimal places
