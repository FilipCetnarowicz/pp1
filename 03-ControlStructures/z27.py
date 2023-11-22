facebook=bool(input("do you have facebook? click enter -no, True - type yes \n"))
twitter=bool(input("do you have twitter? click enter -no, True - type yes \n"))
instagram=bool(input("do you have instagram? click enter -no, True - type yes \n"))
influencePoints=0
if facebook==True:
    influencePoints+=1
if twitter==True:
    influencePoints+=1
if instagram==True:
    influencePoints+=1

print(f"influence points: {influencePoints}")

if influencePoints>=2: print(f"you must be good influencer!")
else: print(f"maybe you would be good influencer if you did some more social media acounts?")
