# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15

arrNor=[15,8,31,47,2,19]
arrRev=[0]*len(arrNor)
for i in range(len(arrNor)):
    arrRev[len(arrNor)-i]=arrNor[i]
print(arrRev)
