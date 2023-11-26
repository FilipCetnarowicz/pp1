PIN="0805"
tries=0
i=0
while i<4:
    tryPin=str(input("insert pin   "))
    if tryPin!=PIN:
        tries+=1
    if tries==3:
        print(f"CARD BLOCKED!")
        break
    if tryPin==PIN:
        print(f"OPENING BANK IN 3 SECONDS")
        break
    i+=1

print("the end")

    
