def saveThePrisoner(n, m, s):
    if (m + s - 1) % n == 0:
        return n
    else:
        return (m + s - 1) % n
print(saveThePrisoner(4,6,2))
#----------------------------------------------------------------------------------------------------
def saveThePrisoner(n, m, s):
    return (m + s - 2) % n + 1
print(saveThePrisoner(4,6,2))