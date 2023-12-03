dec=int(input("type in your decimal number:   "))
rem=0
i=0
binary=""
while dec!=0:
    rem=dec%2
    binary= str(rem) + binary 
    dec=dec//2
    i=i+1

print(f"your binary number: {binary}")