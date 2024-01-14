cars2 = ["ok", "ok", "ok", "ok", "ok"]
cars = ["ok", "ok", "faulty", "ok"]
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
else:
    print("All cars built successfully. No faulty cars!")