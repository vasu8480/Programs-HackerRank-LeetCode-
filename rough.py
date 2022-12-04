def pageCount(n, p):
		mid = (n >> 1)
		trg = (p >> 1) << 1
		return (mid - abs(mid - trg)) >> 1
print(pageCount(6,2))