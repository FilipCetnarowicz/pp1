import math
def f(n):
    if n==0 or n==1:
        return 1
    if n>1:
        return n*f(n-1)

n=6
print("with .math: ",math.factorial(n))
print("with f(n): ", f(n))
