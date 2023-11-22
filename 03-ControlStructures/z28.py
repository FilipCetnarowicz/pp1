# Enter EAN-13 article number: 5901230094938
# Article number is correct
# Article manufactured in Poland

ean= str(input("type your EAN-13 number: "))
eanLen=len(ean)
if ean.isdigit()==True:
    if len(ean)==13:
        print("it is correct lenght EAN-13 code!")
        if ean[:3]=="590":
            print("moreover, this item is from Poland!")

