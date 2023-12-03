amountLeft=int(input("jaką kwotę masz zaplacic? "))
zl5=0
zl2=0
zl1=0
while amountLeft>0:
    if amountLeft>=5:
        zl5+=1
        amountLeft-=5
    elif amountLeft>=2:
        zl2+=1
        amountLeft-=2
    elif amountLeft==1:
        zl1+=1
        amountLeft-=1
print(f"you need to put in \n {zl5}x 5zl coins, \n {zl2}x 2zl coins, \n {zl1}x 1zl coins.")

