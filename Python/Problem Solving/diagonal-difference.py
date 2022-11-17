arr=[[11, 2, 4], [4, 5, 6], [10, 8, -12]]
s=0
d=0
for i in range(len(arr)):
		s+=arr[i][i]
		d+=arr[i][len(arr)-i-1]
print( abs(s-d))	

#-------------------------------------------------------------#
s=0
d=0
for i in range(len(arr)):
		for j in range(0,i+1):
			if i==j:
				s+=(arr[i][j])
		for k in range(len(arr),0,-1):
			if i==len(arr)-k:
				d+=(arr[i][k-1])
print( abs(s-d))