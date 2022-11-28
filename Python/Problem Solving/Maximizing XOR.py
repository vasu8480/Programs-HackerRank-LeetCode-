def maximizingXor(l, r):
	    return max([i^j for i in range(l,r+1) for j in range(l,r+1)])

print(maximizingXor(11,100))
#--------------------------------------------------------------

l,r=11,100
s=0
for i in range(l,r+1):
    for j in range(l,r+1):
        k=i^j
        if k>s:
            s=k
print(s)

