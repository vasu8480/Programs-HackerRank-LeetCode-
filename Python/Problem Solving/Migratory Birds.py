def migratoryBirds(arr):
    s={i:arr.count(i) for i in list(set(arr))}
    m=(max(s.values()))
    return min([k for k,v in s.items() if m==v])

print(migratoryBirds([1,4,4,4,5,3]))