def f(n1,n2):
    for i in range(0,len(n1)):
        for j in range (0,len(n2)):
            if n1[i]==n2[j]:
                return True
    return False
n1=str(input("type n1: "))
n2=str(input("type n2: "))
print(f"result: {f(n1,n2)}")
