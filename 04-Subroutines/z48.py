def f(code):
    sumOfThree=int(code[0])+int(code[1])+int(code[2])
    print(f"sumOfThree={sumOfThree}")
    lastDigit=int(code[3])
    if sumOfThree%7==lastDigit:
        return True
    else:
        return False


code1="7070"
code2="1113"

print(f"code1: {f(code1)}")
print(f"code2: {f(code2)}")