#z29

#declare arrs
#compare with 2nd array by comparing every element from the smaller array to whole second array one by one
# if some number appears - delete it? or make it 0 and then remove all zeros? or 
#best option- create third array, put there values that are !=? but then whats the way to compare

arr1=[4,36,12,28,9,44,5] 
arr2=[5,1,36]
arrResult=[]
for i in arr1:
    if i not in arr2:
        arrResult.append(i)
print(arrResult)