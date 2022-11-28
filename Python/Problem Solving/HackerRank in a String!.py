def hackerrankInString(s):
    a = 'hackerrank'
    i = 0
    for c in s:
        if i < len(a) and c == a[i]:
            i += 1
    return 'YES' if i == len(a) else 'NO'

print(hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'))