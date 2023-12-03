def f(x,y):
    pointss=0
    for i in range(x,y+1):
        print(i)
        if i<0:    
            if i%2==0:
                pointss+=1
    return pointss

x=-6
y=2
print("result: ",f(x,y))
