def countingValleys(steps, path):
    u,d,c=0,0,0
    for i in path:
        if i=='U':
            u+=1
        elif i=='D':
            u-=1
        if u<0:
            d=1
        if(d==1 and u==0):
            c+=1
            d=0
    return c


print(countingValleys(12, "UDDDUDUU"))