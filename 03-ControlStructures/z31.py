x=int(input("type in x axis value   "))
y=int(input("type in y axis value   "))
if x>0 and y>0:
    quadrant="1st quadrant"
elif x<0 and y>0:
    quadrant="2nd quadrant"
elif x<0 and y<0:
    quadrant="3rd quadrant"
elif x>0 and y<0:
    quadrant="4th quadrant"

print(f"P({x},{y}) is in {quadrant}")