#12

# task a
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number) 

# task b
dec=304
print(bin(304))

# task c
dec=304
print(hex(304))

# # task d
# sign="€"
# print(unicode(sign))

# task e
print(abs(-17))


#
import math
dir(math)
#a
print(math.log10(5))
print(math.exp(3))
print(math.sqrt(7))
print(math.sin(3.14/4))

#14

def display_program_name():
    print('Applied informatics')

for i in range(4):
    display_program_name()

#15
def phone_keyboard():
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
phone_keyboard()

#16
def product(x,y):
    return x*y

a = 3
b = 4
print(f"The product of {a} and {b} is {product(a,b)}")
