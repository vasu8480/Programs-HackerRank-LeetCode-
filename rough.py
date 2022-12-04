def saveThePrisoner(n, m, s):
    return (m + s - 2) % n + 1
print(saveThePrisoner(4,6,2))