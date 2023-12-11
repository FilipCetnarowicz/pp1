def display_array(arr):
    print("-----------------------------------------------------------------")
    print("| " + "|  ".join(f"{num:5}" for num in arr) + " |")
    print("-----------------------------------------------------------------")

arr = [1, 23, 5, 382, 1, 17, 4, 906]  # replace this with your array
display_array(arr)