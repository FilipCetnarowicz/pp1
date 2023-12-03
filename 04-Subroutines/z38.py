def f(pal):
    lap=pal[::-1]
    print(pal,lap)
    # lap=""
    # for i in range(0,len(pal),-1):
    #     lap=lap+i
    if pal==lap:
        result=True
    else:
        result=False
    return result

pal0="33-22-33"
pal1="83120"
pal2="book"
pal3="boob"
print(f(pal0))
print(f(pal1))
print(f(pal2))
print(f(pal3))
print(pal2)
print(pal3)