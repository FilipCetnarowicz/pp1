numb=int(input("type number from 1 to 30"))
bingo= 0
points=0
while bingo==0:
    if numb%3==0:
        points+=1
    if numb%5==0:
        points+=1
    if points==2:
        print(f"bingo!!")
        bingo=1
    points=0
    numb=int(input("you lost. try again: type number from 1 to 30"))

print(f"why loop didnt work?")


