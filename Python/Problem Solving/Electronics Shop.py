def getMoneySpent(keyboards, drives, b):
    l=[]
    for i in keyboards:
        for j in drives:
            if i+j<=b:
                l.append(i+j)
    if len(l)>0:
        return (max(l))
    else:
        return -1
print(getMoneySpent([3,1],[5,2,8],10))