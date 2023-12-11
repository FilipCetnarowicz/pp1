def fa(aa):
    firstL=aa[0]
    secondL=aa[0]
    for i in range(len(aa)):
        if aa[i]>=firstL:
            firstL=aa[i]
        if secondL<=aa[i]<=firstL:
            secondL=aa[i]
    return secondL
def fb(bb):
    largestN=bb[0]
    smallestN=bb[0]
    for i in range(len(bb)):
        if bb[i]<=smallestN:
            smallestN=bb[i]
        if bb[i]>=largestN:
            largestN=bb[i]
    return largestN-smallestN
def fc(cc):
    cc.sort()
    if len(cc)%2==0:
        medianaa=(cc[int(len(cc)/2+0.5)]+cc[int(len(cc)/2-0.5)])/2
    else:
        medianaa=cc[int(len(cc)/2)]
    return medianaa
def fd(dd):
    dd.sort()
    return dd[0], dd[-1]
def fe(ee):
    newee=""
    for i in ee:
        newee+=str(i)+"-"
    newee=newee[:-1]
    return (newee)
    # return list(newee)

