import math

a=float(input("Enter a value: "))
b=float(input("Enter b value: "))
c=float(input("Enter c value: "))

s=(a+b+c)/2
triangleArea=math.sqrt(s * (s - a) * (s - b) * (s - c))
triangleCircumference=a+b+c

print("triangle area:", triangleArea)
print("triangle circumference: ", triangleCircumference)