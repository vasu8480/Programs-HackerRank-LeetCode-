n = int(input())
a = set(map(int,input().split()))
for i in range(int(input())):
    op , op_n = input().split()
    l = set(map(int,input().split()))
    eval(f'a.{op}({l})')
print(sum(a))
#-------------------------------------------------- Method 2:
n = int(input())
s = set(map(int, input().split()))
n2 = int(input())
for i in range(n2):
    l = input().split()
    t = set(map(int, input().split()))
    if l[0] == 'update':
        s.update(t)
    elif l[0] == 'intersection_update':
        s.intersection_update(t)
    elif l[0] == 'difference_update':
        s.difference_update(t)
    elif l[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(t)
print(sum(s))