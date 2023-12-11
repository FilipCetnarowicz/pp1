# 34.	Write a program that displays the tuple (10,20,30,40,50) in reverse order. Sample result:
# Tuple: 10,20,30,40,50
# Reverse order: 50,40,30,20,10

t1=(10,20,30,40,50)
ttt=len(t1)
t2=()
for i in reversed(t1):
    t2+=tuple([i])

# t2=[]
# for i in reversed(t1):
#     t2.append(i)
# t2=tuple(t2)

print(t1,t2)




