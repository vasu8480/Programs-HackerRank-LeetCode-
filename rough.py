def circularArrayRotation(a, k, queries):
    # Write your code here
    return [a[(i-k)%len(a)] for i in queries]
print(circularArrayRotation([1,2,3],2,[0,1,2]))