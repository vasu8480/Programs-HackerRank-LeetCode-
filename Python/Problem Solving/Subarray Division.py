s, d, m=[1, 2, 1, 3, 2], 3, 2
c=0
k=0
for i in range(len(s)):
	if sum(s[k:m+k])==d:
		c+=1
	k+=1
print(c)
print(sum(s[1:3]))