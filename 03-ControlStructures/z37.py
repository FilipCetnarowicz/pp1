# while i!=0:
    #     print("* ")
    #     i-=1
asterisks="* "
for i in range(1,10):
    if i<5:
        asterisks=asterisks*i
        print(f"{asterisks}")
        asterisks="* "
    if i>=5:
        i=10-i
        asterisks=asterisks*i
        print(f"{asterisks}")
        asterisks="* "




   
    