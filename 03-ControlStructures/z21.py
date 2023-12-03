x=int(input("prompt first number "))
y=int(input("prompt second number "))
swap=x

if y<x:
    x=y
    y=swap

print(f"smaller number: {x} \n bigger number: {y}")
