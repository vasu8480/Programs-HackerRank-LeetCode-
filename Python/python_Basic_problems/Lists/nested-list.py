if __name__ == '__main__':
    a   ={}
    names = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        a.update({name:score})
    b=sorted(set(a.values()))
    b=b[1]

    names=[]
    for c,k in a.items():
            if k==b:
                names.append(c)
    names.sort()
    for i in names:
        print(i)

#---------------------------------------------------------------------------
if __name__ == '__main__':
    a   ={}
    names = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        a.update({name:score})
    b=sorted(set(a.values()))
    b=b[1]
    a=(sorted ([k for k,v in a.items() if v==b]))
    for i in a:
            print(i)

#---------------------------------------------------------------------------

if __name__ == '__main__':
    a = []
    b = []
    names = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        a.append([name,score])
        b.append(score)
            
    b = sorted(list(set(b)))
    min = b[1]
    
    for i in a:
        if i[1] == min:
            names.append(i[0])
    
    names = sorted(names)
    for name in names:
        print(name) 
