def f(detect):
    peopleInRoom=0
    for i in detect:
        if i=="+":
            peopleInRoom+=1
        elif i=="-":
            peopleInRoom-=1
        if peopleInRoom==-1:
            peopleInRoom+=1
        if peopleInRoom==3:
            return True
    if peopleInRoom<3:
        return False
            
detect1="+--+-+-+--------+++"
print(f(detect1))