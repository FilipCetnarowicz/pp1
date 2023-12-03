def f(x,y):
    ran=[0]*(abs(x-y)+1)
    print(f"ran: {ran}")
    startt=y
    endd=x
    if y>x:
        startt=x
        endd=y
    for i in range(abs(x-y)+1):
        ran[i]=startt+i
    print(f"ran: {ran}")
    ranNarrow=[]
    for i in ran:
        if i%2==0 and i%3==0 and i%4!=0:
            ranNarrow.append(i)
    print(f"ranNarrow: {ranNarrow}")
    return sum(ranNarrow)
x=10
y=30
f(x,y)
print(f(x,y))