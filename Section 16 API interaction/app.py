import requests

APP_ID = "0bf24b2a822d4e47b1482e7ff53db7d2"
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rate = response.json()["rates"]

usd_amount = int(input("Type dollars here: "))
gbp_amount = usd_amount * exchange_rate["GBP"]
print(f"{usd_amount} USD is {gbp_amount} GBP")