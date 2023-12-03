# 0 1 1 2 3 5 8 
fibon=[0,1]
n=20
for i in range(0,n-2):
    fibon.append(fibon[-2]+fibon[-1])

print(f"for {i+1} numbers: {fibon}")