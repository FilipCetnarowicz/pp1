def bubblesort(array):
    n = len(array)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Test the function with three arrays
arr1 = [64, 134, 25, 12, 22, 11, 90]
arr2 = [38, 27, 43, 3, 9, 82, 10]
arr3 = [20, 30, 40, 90, 50, 60, 70]

print("Sorted array 1:", bubblesort(arr1))
print("Sorted array 2:", bubblesort(arr2))
print("Sorted array 3:", bubblesort(arr3))