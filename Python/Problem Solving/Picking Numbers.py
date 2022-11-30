def pickingNumbers(a):
		a.sort()
		m=0
		for i in range(len(a)):
			c=0
			for j in range(i,len(a)):
				if abs(a[i]-a[j])<=1:
					c+=1
			if c>m:
				m=c
		return m

print(pickingNumbers([4, 6, 5, 3, 3, 1]))
#-------------------------------------------------------------------------------
def pickingNumbers(a):
    # Write your code here
    res=1
    for i in range (max(a)+1) :
        res=max(res,a.count(i)+a.count(i+1))
    return res
print(pickingNumbers([1, 2, 2, 3, 1, 2]))