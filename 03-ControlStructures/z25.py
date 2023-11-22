customerBuys=int(input("type amount items you want to buy: "))
price=40

if customerBuys<=2:
    amountToPay=price*customerBuys
elif customerBuys>2:
    amountToPay=2*40+0.75*price*(customerBuys-2)

print(f"after discounts you need to pay {amountToPay} USD.")

