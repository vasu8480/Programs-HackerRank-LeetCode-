x1, v1, x2, v2=0 ,2,5,3
for i in range(10000):
	if x1==x2:
		print("YES")
		break
	x1+=v1
	x2+=v2
else:
	print("NO")