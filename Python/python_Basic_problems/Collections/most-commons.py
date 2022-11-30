from collections import Counter
s = input()
d = Counter(sorted(s)).most_common(3)
[print(x, y) for x, y in d]