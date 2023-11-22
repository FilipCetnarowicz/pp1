
minSpeedLimit = 40
maxSpeedLimit = 140
carSpeed = int(input('Enter car speed km/h: ') )

if carSpeed > maxSpeedLimit:
    print('Warning: speed limit exceeded!!')
elif carSpeed<minSpeedLimit:
    print('Warning: your speed is too low!!')
else: print(f"keep going!")

