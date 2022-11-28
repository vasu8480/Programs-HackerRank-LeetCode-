def camelcase(s):
    s = s[0].upper() + s[1:]
    c=0
    for i in range(len(s)):
        if s[i].isupper():
            c+=1
    return c
print(camelcase('saveChangesInTheEditor'))
#--------------------------------------------------------------------------
import re
def camelcase(s):
    return len(re.findall(r'[A-Z]',s))+1
		
print(camelcase('saveChangesInTheEditor'))