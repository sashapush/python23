import time
from libs.openexchange import OpenExchangeClient

APP_ID = "0bf24b2a822d4e47b1482e7ff53db7d2"

client = OpenExchangeClient(APP_ID)

usd_amount = int(input("Type dollars here: "))
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end-start)  #around 0.5 seconds.

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end-start)

print(f"{usd_amount} USD is {gbp_amount:.2f} GBP") #:.2f - 2 decimal places

