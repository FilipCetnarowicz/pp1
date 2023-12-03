def f(b1,b2,b3,b4):
    points=0
    if b1==True:
        points+=1
    if b2==True:
        points+=1
    if b3==True:
        points+=1
    if b4==True:
        points+=1
    if points>=3:
        return True
    else:
        return False
    
b1=bool(input("input False or True: ").lower()=="true")
b2=bool(input("input False or True: ").lower()=="true")
b3=bool(input("input False or True: ").lower()=="true")
b4=bool(input("input False or True: ").lower()=="true")
f(b1,b2,b3,b4)
print(f"result: {f(b1,b2,b3,b4)}")
