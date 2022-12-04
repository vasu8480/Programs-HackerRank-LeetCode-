def cutTheSticks(arr):
    # Write your code here
    arr.sort()
    result = []
    while len(arr) > 0:
        result.append(len(arr))
        arr = [x - arr[0] for x in arr if x - arr[0] > 0]
    return result

print(cutTheSticks([1 ,2, 3, 4, 3 ,3 ,2 ,1]))
#--------------------------------------------------------------
