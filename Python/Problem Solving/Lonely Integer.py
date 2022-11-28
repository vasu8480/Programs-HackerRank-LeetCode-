def lonelyinteger(a):
		for i in a:
				if a.count(i)==1:
						return i
print(lonelyinteger([1, 1, 2])) # 2

#---------------------------------------------

import collections 
def lonelyinteger(a):
    a=collections.Counter(a)
    for i in a:
        if a[i]==1:
            return i
    
print(lonelyinteger([1, 1, 2])) # 2

