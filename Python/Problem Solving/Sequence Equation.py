def permutationEquation(p):
    l=[]
    for i in range(1,len(p)+1):
        l.append(p.index(p.index(i)+1)+1)
    return l
    
print(permutationEquation([2,3,1]))
#---------------------------------------------------------------------------------------------------
