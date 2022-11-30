import itertools as it
n=int(input())
k=list(map(str,input().split()))
n1=int(input())

a=it.combinations(k,n1) 
l=[]
for i in a:
		l.append("".join(i))
print(l)
d=0
for i in l:
	if 'a' in i:
		d+=1
print(d/len(l))

#-----------------------------------#
import itertools as it
n=int(input())
k=list(map(str,input().split()))
n1=int(input())

a=list(it.combinations(k,n1)) 
d=0
for i in a:
	if 'a' in i:
		d+=1
print(d/len(a))