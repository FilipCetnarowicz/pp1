# 29.	A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes, and wash shoes, which takes 20 minutes. In addition, it is possible to program an additional rinse (15 minutes) and an additional spin (9 minutes). The washing machine settings are saved in variables. Write a program that calculates and displays the total washing time. Sample result:
# washing_product = "shoes"
# rinse = True
# spin = False
# Total washing time: 35 minutes

type=str(input("choose program: jacket 40 min / shoes 20 min / underwear 70 min "))
rinse=bool(input("do you want additional rinse? (15min) - if no - press enter "))
spin=bool(input("do you want additional spin? (9min) - if no - press enter "))

totalTime=0

if type=="jacket":
    totalTime+=40   
elif type=="shoes":
    totalTime+=20
elif type=="underwear":
    totalTime+=70

if rinse==True:
    totalTime+=15

if spin==True:
    totalTime+=9

print(f"total Time of your program: {totalTime} min.")
        
