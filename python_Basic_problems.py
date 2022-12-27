# File: collections-counter.py
from collections import Counter
a=int(input())
b=list(map(int,input().split()))
n=int(input())

c=Counter(b)
total=0
for i in range(n):
    s,p=(map(int,input().split()))
    if c[s]:
        c[s]-=1
        total+=p

print(total)
# File: most-commons.py
from collections import Counter
s = input()
d = Counter(sorted(s)).most_common(3)
[print(x, y) for x, y in d]
# File: word-order.py
import collections 

n=int(input())
l=[]
for i in range(n):
    l.append((input()))

d=collections.Counter(l)
print(len(set(l)))
print(*d.values())
# File: compress-the-string.py
from itertools import groupby

string = input()
print(' '.join( str( (len(list(g)), int(k)) ) for k,g in groupby(string)))

#-----------------------------------------------------------#
print(*[(len(list(g)), int(k)) for k, g in groupby(input())])

# File: iterables-and-iterators.py
import itertools as it
n=int(input())
k=list(map(str,input().split()))
n1=int(input())

a=it.combinations(k,n1) 
l=[]
for i in a:
		l.append("".join(i))
print(l)
d=0
for i in l:
	if 'a' in i:
		d+=1
print(d/len(l))

#-----------------------------------#
import itertools as it
n=int(input())
k=list(map(str,input().split()))
n1=int(input())

a=list(it.combinations(k,n1)) 
d=0
for i in a:
	if 'a' in i:
		d+=1
print(d/len(a))
# File: itertools-combinations-with-replacement.py
from itertools import combinations_with_replacement
n=list(map(str,input().split()))
n1=list(combinations_with_replacement(n[0],int(n[1])))
l=[]
for i in n1:
        l.append(sorted("".join(i)))
l.sort()
for i in l:
    print("".join(i))
#-----------------------------------#

from itertools import combinations_with_replacement
n=list(map(str,input().split()))
n1=list(combinations_with_replacement(n[0],int(n[1])))
l=[ (sorted("".join(i))) for i in n1]
l.sort() 
for i in l:
    print("".join(i))
# File: itertools-combinations.py
from itertools import combinations
s, n = input().split()
s = ''.join(sorted(s))
for i in range(1, int(n)+1):
	print(*sorted(map(''.join, combinations(s, i))), sep = '\n')
# File: itertools-permutations.py
from itertools import permutations
a=input().split()
A = list(permutations(a[0], int(a[1])))
Res = ["".join(A[i]) for i in range(len(A))]
Res.sort()
print("\n".join(Res))
# File: itertools-product.py
from itertools import product
A=map(int,input().split())
B=map(int,input().split())
print(*(product(A,B)))

# File: maximize-it.py
from functools import reduce

n, div = map(int,input().split())
l = []
for i in range(n):
    l.append([int(x)**2 for x in input().split()[1:]])
print(max(map(lambda n: n % div, reduce(lambda a1, a2: list((x+y) for x in a1 for y in a2),l))))
#-----------------------------------#

# File: nested-list.py
if __name__ == '__main__':
    a   ={}
    names = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        a.update({name:score})
    b=sorted(set(a.values()))
    b=b[1]

    names=[]
    for c,k in a.items():
            if k==b:
                names.append(c)
    names.sort()
    for i in names:
        print(i)

#---------------------------------------------------------------------------
if __name__ == '__main__':
    a   ={}
    names = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        a.update({name:score})
    b=sorted(set(a.values()))
    b=b[1]
    a=(sorted ([k for k,v in a.items() if v==b]))
    for i in a:
            print(i)

#---------------------------------------------------------------------------

if __name__ == '__main__':
    a = []
    b = []
    names = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        a.append([name,score])
        b.append(score)
            
    b = sorted(list(set(b)))
    min = b[1]
    
    for i in a:
        if i[1] == min:
            names.append(i[0])
    
    names = sorted(names)
    for name in names:
        print(name) 

# File: divmod.py
print(divmod(177,10))
# File: polar-coordinates.py
from cmath import phase

a=complex(input())
print(abs(complex(a)))
print(phase(complex(a)))

# File: pow.py
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(pow(a, b)+pow(c, d))
#-----------------------------------------------------------#
a=int(input())
b=int(input())
c=int(input())
d=int(input())

print( a**b + c**d)
# File: python-quest-1.py
"""
	1
	22
	333
	4444
"""


for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*((10**i)//9))
#-----------------------------------------------------------#

# File: triangle-quest-2.py
for i in range(1,int(input())+1):
        print(((10**i-1)//9)**2)
#-----------------------------------------------------------#
for i in range(1,int(input())+1):
	print(''.join(map(str,list(range(1,i)))), ''.join(map(str,list(range(i,0,-1)))), sep='')

for i in range(1,int(input())+1):     
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="") 
    print()


# File: no-idea.py
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
A=[1 if i in A else 0 for i in array]
B = [-1 if i in B else 0 for i in array]
print( sum(A) + sum(B))
# File: py-check-strict-superset.py
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
# File: py-set-discard-remove-pop.py
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
# File: py-set-mutations.py
n = int(input())
s = set(map(int,input().split()))
for i in range(int(input())):
    n1 , s2 = input().split()
    l = set(map(int,input().split()))
    eval(f's.{n1}({l})')
print(sum(s))
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
# File: py-the-captains-room.py
from collections import Counter
n = int(input()) # size of the groups
s = list(map(int,input().split()))

c= Counter(s)
for k,v in c.items():
    if v != k and v == 1:
        print(k)
#------------------------------------------------
n = int(input())
s = input().split()
d={}
for i in s:
    if i  in d:
        d[i] += 1
    else:
        d[i] = 1 
c=0
for j,k in d.items():
    if k==1:
        c=j          
print(c)
# File: symmetric-difference.py
n=int(input())
s=set(map(int,input().split()))
n1 = int(input())
s1 = set(map(int,input().split()))
print(*sorted(s^s1), sep='\n')
# File: merge-the-tools.py
#dict.fromkeys()
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        t = string[i: i+k]
        u = list(dict.fromkeys(t))
        print("".join(u))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
# File: python-string-formatting.py
def print_formatted(number):
    pad = len('{0:b}'.format(number))
    for i in range(1,number+1):
        print(str(i).rjust(pad), oct(i)[2:].rjust(pad), hex(i)[2:].upper().rjust            (pad), bin(i)[2:].rjust(pad) )
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
# File: textwrap.py
import textwrap

def wrap(string, max_width):
    a=""
    for i in range(0,len(string),max_width):
        a+=string[i:i+max_width]+"\n"
    return a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)