stocks = {"aapl": 180, "tsla": 250, "msft": 320}
total = 0

print("stock tracker")
while True:

    stock = input("stock name (done to stop):").lower()
    if stock =="done":
        break
    if stock in stocks:
        qty = int(input("quantity:"))
        total += stocks[stock] * qty
        print("Added\n")
    else:
        print("Invalid stock\n")

print("Total Investment:",total)

with open("portfolio.txt","w") as f:
    f.write(f"Total:{total}")
    
print("saved in file")