def month(n):
    monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return monthName[n-1]
#Enter month number: 10
monthNum=10
print(f"{monthNum}th month name: {month(monthNum)}")

