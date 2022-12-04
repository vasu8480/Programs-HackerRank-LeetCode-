def hurdleRace(k, height):
    # Write your code 
    m=max(height)
    if m>k:
        return m-k
    else:
        return 0

print(hurdleRace(4,[1,6,3,5,2]))