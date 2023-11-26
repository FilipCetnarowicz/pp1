a=int(input("a: ")) #15 gorna krawedz
b=int(input("b: ")) #4 boczna krawedz


for i in range(1,b+1):
    if i==1 or i==b:
        print("*"*a)
    else:
        print("*"," "*(a-4),"*")



