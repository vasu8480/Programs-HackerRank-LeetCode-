n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
A=[1 if i in A else 0 for i in array]
B = [-1 if i in B else 0 for i in array]
print( sum(A) + sum(B))