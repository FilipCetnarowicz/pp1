
print('hello world!')

if 5 > 2:
    print("Five is greater than two!")

# this is a comment
x = 5
y = "Hello, World!"

#print("Hello, World!")
print("Cheers, Mate!")

"""
multiline string
yeah
"""

x = str(12)    # x will be '3'
y = int(3)    # y will be 3
z = float(3+3)  # z will be 3.0
print(x,y,z)

x= str('3')
print(x)
print(type(x))

A=4
a=5
print(f'a={a}, A={A}')

x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)

print("python "+"is "+"awesome!")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#~~~~~~~~~~~~~~~~~~~~~~~~~~
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
x=random.randrange(1,3)
print(x,x,x,x,x,x,x)
print(type(x))
x=float(x)
print(type(x),x,x,x,x,x)

x = ["apple", "banana", "cherry"]
print(type(x))

x=str(1)
print(x)

a= """this
is 
multiple line string"""
print(a)
print(a[0])

for x in "banana":
  print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = " Hello, World! "
print(b[-2:-5])

print(b.upper())

print(b.lower())


print(b.split(","))


print(b.replace("H","Y"))

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


print(b.split())

