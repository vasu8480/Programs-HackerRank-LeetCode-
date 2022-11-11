n = int(input())
s = set(map(int,input().split()))
for i in range(int(input())):
    n1 , s2 = input().split()
    l = set(map(int,input().split()))
    eval(f'a.{n1}({l})')
print(sum(s))