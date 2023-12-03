file=open("z11.txt",'r')
theSum=0
numbers=""
for i in file:
    numbers+=str(i)
    print(i,end="")
    theSum+=int(i)
print()
#zamienic endl na ","
# " ".join(numbers)
print(f"numbers: {numbers}")
print(f"sum: {theSum}")
file.close()
