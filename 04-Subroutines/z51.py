def f(n):
    if n<=1:
        return 0
    else:
        return n+f(n-1)

n=7
print(f"f(n)= {f(n)}")
print("n=10 ->",f(10))