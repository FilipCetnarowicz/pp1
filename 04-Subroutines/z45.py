def oper(equation):
    if equation[0].isdigit():
        equation="+"+equation

    equationNew=list(equation)
    equNew=[0]*(len(equationNew)//2)
    result=0

    print(f"equNew: {equNew}")
    print(f"equationNew: {equationNew}")
   
    for i in range(1,len(equation),2):
        if equationNew[i-1]=="-":
            sign=-1
        elif equationNew[i-1]=="+":
            sign=1
        equNew[i//2]=int(equationNew[i])*sign
    print(f"equNew: {equNew}")

    for i in equNew:
        result+=i
    return result

equation="1+4-3"
print(oper(equation))


