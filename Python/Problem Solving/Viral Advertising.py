def viralAdvertising(n):
    shared = 5
    liked = 0
    cumulative = 0
    for i in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative
print(viralAdvertising(3))