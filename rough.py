arr=[[11, 2, 4], [4, 5, 6], [10, 8, -12]]

s=0
d=0
for i in range(len(arr)):
		s+=arr[i][i]
		d+=arr[i][len(arr)-i-1]
print( abs(s-d))	