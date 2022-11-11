n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    l=input().split()
    try:
        if l[0] == 'pop':
                s.pop()
        elif l[0] == 'remove':
                s.remove(int(l[1]))
        elif l[0] == 'discard':
            s.discard(int(l[1]))
    except Exception as e:
            continue 
print(sum(s))