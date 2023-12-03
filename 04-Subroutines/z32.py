def f(x,y,z):
    points=0
    if x<0:
        points+=1
    elif y<0:
        points+=1        
    elif z<0:
        points+=1
    if points>=1:
        return True
    else:
        return False

x=5
y=3
z=0
print(f(x,y,z))