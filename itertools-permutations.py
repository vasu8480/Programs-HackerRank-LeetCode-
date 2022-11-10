from itertools import permutations
a=input().split()
A = list(permutations(a[0], int(a[1])))
Res = ["".join(A[i]) for i in range(len(A))]
Res.sort()
print("\n".join(Res))