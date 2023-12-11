arr=[[1,3,5],[8,7,2]]
# a.	Sum of the first element in the first row and the last element in the last row
# b.	Sum of the elements in the middle column
# c.	Sum of the elements in the last row
# Sample result:
# 3
# 10
# 17
print(f"a. 1st- {arr[0][0]}, 2nd - {arr[-1][-1]}, sum= {arr[0][0]+arr[-1][-1]}")
print(f"a. 1st- {arr[0][1]}, 2nd - {arr[1][1]}, sum= {arr[0][1]+arr[1][1]}")
print(f"a. 1st- {arr[-1][0]}, 2nd - {arr[-1][1]}, 3rd - {arr[-1][2]}, sum={sum(arr[1])}")

