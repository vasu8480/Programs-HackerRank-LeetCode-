def utopianTree(n):
		height = 1
		for i in range(n):
				if i % 2 == 0:
						height *= 2
				else:
						height += 1
		return height
print(utopianTree(0))