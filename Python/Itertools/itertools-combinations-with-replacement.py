from itertools import combinations_with_replacement
n=list(map(str,input().split()))
n1=list(combinations_with_replacement(n[0],int(n[1])))
l=[]
for i in n1:
        l.append(sorted("".join(i)))
l.sort()
for i in l:
    print("".join(i))
#-----------------------------------#

from itertools import combinations_with_replacement
n=list(map(str,input().split()))
n1=list(combinations_with_replacement(n[0],int(n[1])))
l=[ (sorted("".join(i))) for i in n1]
l.sort() 
for i in l:
    print("".join(i))