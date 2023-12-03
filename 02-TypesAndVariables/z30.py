import random
diceRoll1=random.randint(1,6)
specialNumb= diceRoll1==1 or diceRoll1==6

print(f"Dice rolled: {diceRoll1}")
print(f"Special number: {specialNumb}")