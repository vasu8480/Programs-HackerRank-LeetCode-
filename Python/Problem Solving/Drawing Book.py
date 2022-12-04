def pageCount(n, p):
    if n % 2 == 0:
                n += 1
    return min(p // 2, n // 2 - p // 2)
print(pageCount(6,2))

#--------------------------------------------------------------
def pageCount(n, p):
		mid = (n >> 1)
		trg = (p >> 1) << 1
		return (mid - abs(mid - trg)) >> 1
print(pageCount(6,2))