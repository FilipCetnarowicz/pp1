
currentPrice=float(input("how much is it now?"))
oldPrice=float(input("how much it was before?"))

difference=oldPrice-currentPrice
discount=difference/oldPrice*100
economic=bool
if discount<=10:
    economic=True
else:
    economic=False

if economic==False:
    print(f"Current product price: {currentPrice}, Previous product price: {oldPrice}, so discount level is: {discount}% !! But it now!!")
else:
    print(f"Current product price: {currentPrice}, Previous product price: {oldPrice}, so discount level is: {discount}%. You can buy now or wait for upcoming sales.")