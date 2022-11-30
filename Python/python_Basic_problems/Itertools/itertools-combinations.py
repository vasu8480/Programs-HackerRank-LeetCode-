from itertools import combinations
s, n = input().split()
s = ''.join(sorted(s))
for i in range(1, int(n)+1):
	print(*sorted(map(''.join, combinations(s, i))), sep = '\n')