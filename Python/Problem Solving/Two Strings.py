def twoStrings(s1, s2):
    a=set(s1) &set(s2)
    if len(a)>0:
        return 'YES'
    else:
        return 'NO'

print(twoStrings('hello','world'))

#-------------------------------------------------------------------------
def twoStrings(s1, s2):
		return 'YES' if set(s1) &set(s2) else 'NO'
print(twoStrings('hello','world'))