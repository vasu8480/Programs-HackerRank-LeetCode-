def counterGame(n):
    s = bin(n)
    return 'Louise' if (s.count('1') + s[:1:-1].find('1')) % 2 == 0 else 'Richard'
print(counterGame(6))