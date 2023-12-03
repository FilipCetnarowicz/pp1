def f(x,y):
    even=""
    odd=""
    if y==True:
        for i in x:
            if int(i)%2==0:
                even+=i
        even="+".join(even)
        even=eval(even)
        return even
    elif y==False:
        for i in x:
            if int(i)%2!=0:
                odd+=i
        odd="+".join(odd)
        odd=eval(odd)
        return odd    
    
numberr="3124"
evenn=True
print(f(numberr,evenn))