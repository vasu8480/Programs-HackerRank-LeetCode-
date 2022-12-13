def mergeSort(arr):
    if len(arr) == 1:
        return arr
    midPoint = int(len(arr)/2)
    leftPart = arr[:midPoint]
    rightPart = arr[midPoint:]
    return merge(mergeSort(leftPart), mergeSort(rightPart))

def merge(arr1, arr2):
    firstPointer = 0
    secondPointer = 0
    mergedList = []

    while firstPointer < len(arr1) and secondPointer < len(arr2):
        if arr1[firstPointer] < arr2[secondPointer]:
            mergedList.append(arr1[firstPointer])
            firstPointer += 1
        else:
            mergedList.append(arr2[secondPointer])
            secondPointer += 1
    
    while firstPointer < len(arr1):
        mergedList.append(arr1[firstPointer])
        firstPointer += 1
    while secondPointer < len(arr2):
        mergedList.append(arr2[secondPointer])
        secondPointer += 1
    return mergedList

print(mergeSort([8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))

def quickSort(arr, left=0, right=None):
    if right == None:
        right = len(arr) - 1
    if left < right:
        pivotIndex = pivot(arr, left, right)
        quickSort(arr, left, pivotIndex-1)  
        quickSort(arr, pivotIndex+1, right)       
    return arr

def pivot(arr, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex+1, endIndex+1):
        if arr[i] < arr[pivotIndex]:
            swapIndex += 1
            arr[swapIndex], arr[i] = arr[i], arr[swapIndex]
    arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]
    return swapIndex

print(quickSort([8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))

def heapSort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr

def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

print(heapSort([8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))