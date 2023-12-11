def issSubset(a1,a2):
    a1=set(a1)
    a2=set(a2)
    if a2.issubset(a1):
        return True
    else:
        return False

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]
print(issSubset(arr1, arr2))