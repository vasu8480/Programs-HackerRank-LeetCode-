import re


def camelcase(s):
    return len(re.findall(r'[A-Z]',s))+1
print(camelcase('saveChangesInTheEditor'))