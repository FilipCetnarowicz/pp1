# print("z8")
# speedLimit=140
# carSpeed=int(input("enter your car speed limit km/h"))

# if carSpeed > speedLimit:
#     print('Warning: speed limit exceeded!!')
# else:
#     print(f"carSpeed: {carSpeed}")

# print("z9")
# #v1=input(bool())
# #v2=input(bool())
# #v3=input(bool())
# #v4=input(bool())
# #testPass=[v1,v2,v3,v4]
# #if sum(testPass)>2:
# #    print("test passed")
# #else:
# #    print("test failed")

# print("z10")
# enterNumber=int(input("enter negative number to convert to positive"))
# print(f"absolute value: {abs(enterNumber)}")

# print("z11")

# enNum=int(input())
# if enNum%2 == 0:
#     print("your number is even")
# else:
#     print("your number is odd")

# print("z12")
# n1=input("Enter first person name: ")
# a1=int(input("Enter first person age: "))
# n2=input("Enter second person name: ")
# a2=int(input("Enter second person age: "))
# if a1>=18 and a2>=18:
#     print(f"Both {n1} and {n2} are adults ")
# else:
#     print("someone isnt adult ")

# print("z13")

#LOOOOOPS

print("z14")
i = 1
while i <= 4:
    print('Practice makes perfect!!')
    i = i + 1

print("z15")
for i in range(4):
    print('Practice makes perfect!')

print("z16")
sum = 0
for i in range(1,6):
    print(i)
    sum = sum + i
print(f'Sum is {sum}')

print("z17")
sum = 0
i=1
while i<6:
    print(f"i= {i}")
    sum = sum + i
    i=i+1
print(f'Sum is {sum}')

print("z18")
l=1
m=1
while m<11:
    print(f"l={l}/m={m}= {l/m}")
    m=m+1

l=1
m=1
for m in range(1,11):
    print(f"l={l}/m={m}= {l/m}")

print("z19")
#19.	Write a program that calculates the 
# sum of even numbers in the range <1,10>.
sum=0
for i in range (1,11):
    if i%2==0:
        sum=sum+i
print(f"sum is {sum}")