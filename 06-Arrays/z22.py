# tactic: 
arr=[8,2,5,1,9]
arrPow=[0]*len(arr)
for i in range(len(arr)):
    arrPow[i]=pow(arr[i],2)
print(arrPow)