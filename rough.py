l,r=11,100

l=min(l,r)
r=max(l,r)
s=0
for i in range(l,r+1):
    for j in range(l,r+1):
        k=i^j
        if k>s:
            s=k
print(s)
    

    