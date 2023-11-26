print("bingo 20.11 code: \n")
bingo= 0
points=0

for i in range(1,31):
    if i%5==0 and i%3==0:
        print("BINGOOOOO!!")
    elif i%5==0:
        print(f"FIVE")
    elif i%3==0:
        print(f"THREE")
    else: print(f"{i}")
    


