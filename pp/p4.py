def f(n):
    if n%2==0:
        n=n*(-1)
        return n
    elif n%2!=0:
        n=abs(n)
        return n

n=int(input("type number: "))
print(f(n))