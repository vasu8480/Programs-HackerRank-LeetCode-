def utopianTree(n):
		height = 1
		for i in range(n):
				if i % 2 == 0:
						height *= 2
				else:
						height += 1
		return height
print(utopianTree(4))

#--------------------------------------------------------------------------------------------------------------
def utopianTree(n):
    # Write your code here
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (1+utopianTree(n-1))
    else:
        return (2 * utopianTree(n-1))
print(utopianTree(4))