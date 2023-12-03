def f(n1,n2,op):
    if op=="+":
        result=n1+n2
        return result
    if op=="-":
        result=n1-n2
        return result
    if op=="%":
        result=n1%n2
        return result
    if op=="*":
        result=n1*n2
        return result
    if op=="**":
        result=n1**n2
        return result

n1=2
n2=3
op="**"            
#[+,-,*,%,**]
print(f(n1,n2,op))