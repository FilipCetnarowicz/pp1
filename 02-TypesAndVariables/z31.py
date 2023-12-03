import random
diceRoll=random.randint(1,6)
diceGuess=int(input("type your guess "))
rightGuess= diceGuess==diceRoll

print(f"dice roll: {diceRoll}, your guess: {diceGuess}, did you win?: {rightGuess}")
