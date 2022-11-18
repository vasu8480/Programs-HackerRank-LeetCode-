a,b=[2, 4], [16, 32, 96]
s=0
for i in range(max(a), min(b)+1):
		for k in a:
				if i % k != 0:
						break	
		else:
				for k in b:
						if k % i != 0:
								break
				else:
						s+=1
print(s)