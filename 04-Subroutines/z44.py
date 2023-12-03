def f(passw):
    uniCharacters=[]
    for i in passw:
        if i not in uniCharacters:
            uniCharacters+=i
    if len(uniCharacters)>=6:
        return True
    else:
        print("try again")
        return False
        
passw="book13"
print(f"password is {f(passw)}")