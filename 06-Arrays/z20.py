arr=[34,7,19,4,21,8]
oddNum=0
i=0
while i<len(arr):
    if arr[i]%2!=0:
        oddNum+=1
    i+=1

print(oddNum)