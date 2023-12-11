# 23.	An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and displays the maximum and minimum number. Do not use available functions.

arr=[-15, 8, -31, 47, -2, 19]
lowestt=arr[0]
highestt=arr[0]
for i in arr:
    if i<lowestt:
        lowestt=i
    if i>highestt:
        highestt=i
print(lowestt, highestt)