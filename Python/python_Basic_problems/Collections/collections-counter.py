from collections import Counter
a=int(input())
b=list(map(int,input().split()))
n=int(input())

c=Counter(b)
total=0
for i in range(n):
    s,p=(map(int,input().split()))
    if c[s]:
        c[s]-=1
        total+=p

print(total)