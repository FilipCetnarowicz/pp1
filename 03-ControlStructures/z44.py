x=[1,2,2,3,0,5]
summ=0
mean=0
i=0
for nr in x:
    print(nr)
    if nr==0:
        print("STOP!!")
        break
    summ+=nr
    print(f"sum = {summ}")
    mean=summ/(nr+1)
    print(f"mean = {mean}")
    i+=1
    print(i)
    print()



