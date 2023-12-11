import random

arr1=[3,7,1,0,4]
print(f"arr1: {arr1}")

arr2=[[2,3],[7,1],[0,4]]
print(f"arr2: {arr2}")

arr3=[7 for i in range(5)]
print(f"arr3: {arr3}")

arr4=[i for i in range(1,10)]
print(f"arr4: {arr4}")

arr5=[i*2 for i in range(1,10)]
print(f"arr5: {arr5}")

arr6=[random.randint(1,20) for i in range(10)]
print(f"arr6: {arr6}")

arr7=[[] for i in range(5)]
print(f"arr7: {arr7}")

arr14=[[False for i in range(2)]for j in range(5)]
print(f"arr14: {arr14}")
