ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

s={}.fromkeys(ar,0)
for i in ar:
		s[i]+=1
print(s)
c=0
for i in s.values():
	while i>=2:
		c+=1
		i=i-2
print(c)
