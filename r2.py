n=13
a=[x for x in range(1,n+1)]
print(a)

#count number of elements that has 1 in it
print(sum([1 for x in a if '1' in str(x)]))