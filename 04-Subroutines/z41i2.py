
def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n>2:
        for i in range(2,n):
            if n%i==0:
                return False
    return True

def NthPrime(num):
    count=0
    numb=2
    while True:
        if isPrime(numb):
            count+=1
            if count==num:
                return numb
        numb+=1

num=int(input("num - nth prime number: "))
print(f"{num}'th prime number is: {NthPrime(num)}")