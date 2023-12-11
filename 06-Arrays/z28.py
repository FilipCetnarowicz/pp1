def compare(a1,a2):
    if len(a1)!=len(a2):
        return False
    for i in range(len(a1)):
        if a1[i]!=a2[i]:
            return False
    return True

# 28.	Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise.  Two arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal. Then create a program and try to compare the following arrays: 
# a.	["water","book","sky"]   ["water","book","sky"]
# b.	[True,False]   [True,False,True]
# c.	[5,3,1]   [5,3,1]
# d.	[3,2,1]   [3,2]

a1=["water","book","sky"]   
a2=["water","book","sky"]

# b.	
b1=[True,False]   
b2=[True,False,True]

print(compare(a1,a2))
print(compare(b1,b2))


