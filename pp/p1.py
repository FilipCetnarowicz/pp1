def f(n):
    # 0 1 1 2 3 5 8
    enn=[0]*n
    enn[0]=0
    enn[1]=1
    for i in range(2,n):
        enn[i]=enn[i-1]+enn[i-2]
        # print(f"enn: {enn[i]}")
    return enn

n=int(input("n: "))
f(n)
print(f"odp: {f(n)}")