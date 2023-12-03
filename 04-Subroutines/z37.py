def f(n):
    fib=[0]*n
    fib[0]=0
    fib[1]=1
    for i in range(2,n):
        fib[i]=fib[i-1]+fib[i-2]
    print(fib)
    return fib[-1]
print(f(3)) #
print(f(5)) #3
print(f(9)) #21
# 0 1 1 2 3 5 8 13 21