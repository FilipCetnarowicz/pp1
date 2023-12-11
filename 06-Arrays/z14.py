# 14.	An array contains values: [[2,5,4],[9,0,3]]. Create a program that displays:
# a.	the array
# b.	size of the array (number of rows and columns)
# c.	value 5 from the array
# d.	value 3 from the array
# e.	second row of the array as below:
# 9 0 3

arr=[[2,5,4],[9,0,3]]
print(f"a. {arr}")
print(f"b. rows: {len(arr)}, cols:{len(arr[0])}")
print(f"c. {arr[0][1]}")
print(f"d. {arr[1][2]}")
print(f"e. {arr[1]}")
