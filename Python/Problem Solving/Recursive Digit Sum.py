def superDigit(n, k):
    if len(n) == 1:
        return n
    else:
        return superDigit(str(sum([int(i) for i in n]) * k), 1)
print(superDigit('148', 3))