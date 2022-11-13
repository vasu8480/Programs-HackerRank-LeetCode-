import collections 

n=int(input())
l=[]
for i in range(n):
    l.append((input()))

d=collections.Counter(l)
print(len(set(l)))
print(*d.values())