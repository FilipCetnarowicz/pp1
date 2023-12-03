def f(t):
    t=list(t)
    for i in range(0,len(t)):
        t[i]=(i)*t[i]
    t=str(t)
    t.join("-")
    return t[i]



t="okej"
print(f(t))