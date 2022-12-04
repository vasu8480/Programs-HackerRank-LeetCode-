def circularArrayRotation(a, k, queries):
    # Write your code here
    for i in range(k):
        a.insert(0,a.pop())
    return [a[i] for i in queries]
print(circularArrayRotation([1,2,3],2,[0,1,2]))
#----------------------------------------------------------------------------------------------------
def circularArrayRotation(a, k, queries):
    # Write your code here
    return [a[(i-k)%len(a)] for i in queries]
print(circularArrayRotation([1,2,3],2,[0,1,2]))