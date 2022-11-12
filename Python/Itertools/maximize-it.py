from functools import reduce

n, div = map(int,input().split())
l = []
for i in range(n):
    l.append([int(x)**2 for x in input().split()[1:]])
print(max(map(lambda n: n % div, reduce(lambda a1, a2: list((x+y) for x in a1 for y in a2),l))))
#-----------------------------------#
