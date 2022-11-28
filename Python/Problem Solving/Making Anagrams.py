def makingAnagrams(s1, s2):
    # Write your code here
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    i,j=0, 0
    count = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif s1[i] < s2[j]:
            count += 1
            i += 1
        else:
            count += 1
            j += 1
    if i < len(s1):
        count += len(s1) - i
    if j < len(s2):
        count += len(s2) - j
    return count

print(makingAnagrams('absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'))
