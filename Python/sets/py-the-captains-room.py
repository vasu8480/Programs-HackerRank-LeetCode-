from collections import Counter
n = int(input()) # size of the groups
s = list(map(int,input().split()))

c= Counter(s)
for k,v in c.items():
    if v != k and v == 1:
        print(k)
#------------------------------------------------
n = int(input())
s = input().split()
d={}
for i in s:
    if i  in d:
        d[i] += 1
    else:
        d[i] = 1 
c=0
for j,k in d.items():
    if k==1:
        c=j          
print(c)