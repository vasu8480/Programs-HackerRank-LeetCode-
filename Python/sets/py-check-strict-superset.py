A = set(map(int, input().split()))
B = [set(map(int, input().split())) for i in range(int(input()))]
result = all([A.issuperset(b) and len(A) > len(b) for b in B])

print(result)
#--------------------------------------------------
s = set(map(int,input().split()))
n = int(input()) # number of other sets
result = True
for i in range(n):
    x=set(map(int,input().split()))
    if not (s.issuperset(x)):
        result = False
print(result)