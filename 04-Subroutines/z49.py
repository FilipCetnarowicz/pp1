def f(dice):
#def f(ice): 
   # dice=list(map(int,ice))
    print(dice)
    winner=""
    winnerScore=0
    currentScore=1
    for i in range(1,len(dice)):
        if dice[i] == dice[i-1]:
            currentScore+=1
        else:
            if winnerScore<=currentScore:
                winner=dice[i-1]
                winnerScore=currentScore
            currentScore=1
    return f"winner is number {winner} with {winnerScore} points"

dice1="1127345000012965"
dice2="91257788079790"

print(f(dice2))