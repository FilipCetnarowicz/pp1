def f1(t):
    t=t.split()
    print(t)
    return len(t)
def f2(t):
    t=t.split()
    return sorted(t, key=len, reverse=True)
def f3(t):
    t=t.split()
    t.sort(key=len)
    return t 
# def f3(t):

textt="An apple a day keeps the doctor away"
print(f1(textt))
print(f2(textt))
print(f3(textt))