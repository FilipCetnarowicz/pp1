# Enter the dog's age in human years: 15
# The dog's age in dog’s years is 73 years.

yearAge=float(input("type dog's age: "))
if yearAge<=2.0:
    dogAge=yearAge*10.5
elif yearAge>2.0:
    dogAge=2*10.5+(yearAge-2)*4

print(f"this dog who is {yearAge} years old in human years, is {dogAge} years old in dogs' years")

