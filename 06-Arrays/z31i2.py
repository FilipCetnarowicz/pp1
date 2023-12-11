# arr1=[2, 3, 2, 5, 8, 1, 9, 8]
# arr2=[] #with those that appear twice
# arr3=[]
# for i in arr1:
#     if i not in arr2:
#         arr2.append(i)
# for i in arr2:
#     if i in arr1:
#         arr3.append(i)
# print(arr1)
# print(arr2)
# print(arr3)

#wont work

arr1=[2, 3, 2, 5, 8, 1, 9, 8]
arr2=[]

for i in arr1:
    # if (i not in arr2) and (arr1.count(i)==1):
    if arr1.count(i)==1:
        arr2.append(i)
print(arr1)
print(arr2)