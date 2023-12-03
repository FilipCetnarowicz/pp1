def f(x):
    patternn=""
    for i in range(x):
        patternn+="*"
    print(patternn)
    patternn="/".join(patternn)
    print(patternn)
    return patternn
x=5
print(f(x))