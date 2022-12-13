class Sorting_Algorithms:
    # Bubble Sort
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: compare adjacent elements and swap them if they are in wrong order
    #time complexity: O(n^2)
    def bubbleSort(self,arr):
        for i in range(len(arr) - 1, 0 ,-1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    # Selection Sort
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: find the minimum element in unsorted array and swap it with element at beginning
    #time complexity: O(n^2)
    def selectionSort(self,arr):
        for i in range(len(arr)-1):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr
        #-------------------------OR-------------------------
    def selectionSort2(self,arr):
        for i in range(len(arr)):
            min_val=min(arr[i:])
            min_ind=arr.index(min_val)
            arr[i],arr[min_ind]=arr[min_ind],arr[i]
        return arr
    
    # Insertion Sort
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: insert each item into its proper place to form the sorted list
    #time complexity: O(n^2)
    def insertionSort(self,arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i-1
            while temp < arr[j] and j > -1:
                arr[j+1] = arr[j] 
                arr[j] = temp
                j -= 1
        return arr
    
    # Merge Sort
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: divide and conquer
    #time complexity: O(nlogn)

    def mergeSort(self,arr):
        if len(arr) == 1:
            return arr
        midPoint = int(len(arr)/2)
        leftPart = arr[:midPoint]
        rightPart = arr[midPoint:]
        return self.merge(self.mergeSort(leftPart), self.mergeSort(rightPart))

    def merge(self,arr1, arr2):
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

    #pivot
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: divide and conquer
    #time complexity: O(nlogn)
    def pivot(self, arr, pivotIndex, endIndex):
        swapIndex = pivotIndex
        for i in range(pivotIndex+1, endIndex+1):
            if arr[i] < arr[pivotIndex]:
                swapIndex += 1
                arr[swapIndex], arr[i] = arr[i], arr[swapIndex]
        arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]
        return swapIndex

    def quickSort(self,arr, leftPointer = 0, rightPointer=None):
        if rightPointer == None:
            rightPointer = len(arr) - 1
        if leftPointer < rightPointer:
            pivotIndex = self.pivot(arr, leftPointer, rightPointer)
            self.quickSort(arr, leftPointer, pivotIndex-1)  
            self.quickSort(arr, pivotIndex+1, rightPointer)       
        return arr

    #Heapify
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: heapify means to create a heap from the array
    #time complexity: O(nlogn)
    def heapify(self,arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    def heapSort(self,arr):
        n = len(arr)

        # Build a MAX_HEAP.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        # Swap nodes with root to sort
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr

s=Sorting_Algorithms()
print(s.bubbleSort([8,69,89,85,7885,146,4,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))
print(s.selectionSort([8,69,89,85,7885,146,4,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))
print(s.selectionSort2([8,69,89,85,7885,146,4,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))
print(s.insertionSort([8,69,89,85,7885,146,4,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))
print(s.mergeSort([8,69,89,85,7885,146,4,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))
print(s.quickSort([8,69,89,85,7885,146,4,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))
print(s.heapSort([8,69,89,85,7885,146,4,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]))