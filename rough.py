class Sorting_Algorithms:
    # Bubble Sort
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: compare adjacent elements and swap them if they are in wrong order
    #time complexity: O(n^2)
    def bubbleSort(self,arr):
        for i in range(len(arr) - 1, 0 ,-1): # 0 to n-1
            for j in range(i): # 0 to n-1
                if arr[j] > arr[j+1]: # swap if greater
                    arr[j], arr[j+1] = arr[j+1], arr[j] # swap
        return arr
    
    # Selection Sort
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: find the minimum element in unsorted array and swap it with element at beginning
    #time complexity: O(n^2) 
    def selectionSort(self,arr):
        for i in range(len(arr)-1): # loop through all elements
            minIndex = i # assume first element is the smallest
            for j in range(i+1, len(arr)): # loop through unsorted part
                if arr[j] < arr[minIndex]: # if smaller element is found
                    minIndex = j # set new minIndex
            arr[i], arr[minIndex] = arr[minIndex], arr[i] # swap
        return arr
        #-------------------------OR-------------------------
    def selectionSort2(self,arr):
        for i in range(len(arr)): # loop through all elements 
            min_val=min(arr[i:]) # find the minimum element in unsorted array
            min_ind=arr.index(min_val) # find the index of minimum element
            arr[i],arr[min_ind]=arr[min_ind],arr[i] # swap
        return arr 
    
    # Insertion Sort
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: insert each item into its proper place to form the sorted list
    #time complexity: O(n^2) 
    def insertionSort(self,arr):
        for i in range(1, len(arr)): # loop through all elements
            temp = arr[i] # store current element whose left side is checked for its
            j = i-1 # left side of the array is checked for its proper position
            while temp < arr[j] and j > -1: # check whether the adjacent element in left side is greater or not
                arr[j+1] = arr[j]  # shift the element to one position right
                arr[j] = temp # if the adjacent element is greater, shift it to one position right
                j -= 1 # repeat the loop until the element is in its proper position
        return arr
    
    # Merge Sort
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: divide and conquer
    #time complexity: O(nlogn) worst case: O(nlogn)

    def mergeSort(self,arr):
        if len(arr) == 1: # base case
            return arr
        midPoint = int(len(arr)/2) # find the mid point
        leftPart = arr[:midPoint] # left part of the array 
        rightPart = arr[midPoint:] # right part of the array
        return self.merge(self.mergeSort(leftPart), self.mergeSort(rightPart)) # merge the sorted left and right parts

    def merge(self,arr1, arr2):
        firstPointer = 0 # pointer for left part
        secondPointer = 0 # pointer for right part
        mergedList = [] 

        while firstPointer < len(arr1) and secondPointer < len(arr2): # loop until one of the pointer reaches the end
            if arr1[firstPointer] < arr2[secondPointer]: # compare the elements pointed by the two pointers
                mergedList.append(arr1[firstPointer]) # append the smaller element to the merged list
                firstPointer += 1 # increment the pointer
            else:
                mergedList.append(arr2[secondPointer]) # append the smaller element to the merged list
                secondPointer += 1 # increment the pointer

        while firstPointer < len(arr1): # if there are any elements left in the left part
            mergedList.append(arr1[firstPointer]) # append them to the merged list
            firstPointer += 1

        while secondPointer < len(arr2):
            mergedList.append(arr2[secondPointer]) # append them to the merged list
            secondPointer += 1

        return mergedList

    #pivot
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: divide and conquer
    #time complexity: O(nlogn) 
    # worst case: O(n^2) -when the sorted array is passed
    def pivot(self, arr, pivotIndex, endIndex):
        swapIndex = pivotIndex  # swapIndex is the index of the element that is smaller than the pivot element
        for i in range(pivotIndex+1, endIndex+1):   
            if arr[i] < arr[pivotIndex]:    # if the element is smaller than the pivot element
                swapIndex += 1            # increment the swapIndex
                arr[swapIndex], arr[i] = arr[i], arr[swapIndex] # swap the element with the element pointed by the swapIndex
        arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]   # swap the pivot element with the element pointed by the swapIndex
        return swapIndex

    def quickSort(self,arr, leftPointer = 0, rightPointer=None):
        if rightPointer == None:    # if rightPointer is not passed
            rightPointer = len(arr) - 1 # set rightPointer to the last index of the array
        if leftPointer < rightPointer:  
            pivotIndex = self.pivot(arr, leftPointer, rightPointer) # get the pivotIndex
            self.quickSort(arr, leftPointer, pivotIndex-1)      # sort the left part of the array
            self.quickSort(arr, pivotIndex+1, rightPointer)    # sort the right part of the array
        return arr

    #Heapify
    # arr=[8,69,89,85,7885,146,98,464,678,648,875,47,845,8474,854,785,74,548,44,78,75]
    #approach: heapify means to create a heap from the array
    #time complexity: O(nlogn) worst case: O(nlogn)
    def heapify(self,arr, n, i):
        largest = i # Initialize largest as root
        l = 2 * i + 1 # left child index
        r = 2 * i + 2 # right child index

        if l < n and arr[largest] < arr[l]: # check if left child is larger than root
            largest = l # change the largest index

        if r < n and arr[largest] < arr[r]: # check if right child is larger than root
            largest = r # change the largest index

        if largest != i:    # if largest is not root
            arr[i], arr[largest] = arr[largest], arr[i] # swap
            self.heapify(arr, n, largest)   # heapify the root
            
    def heapSort(self,arr):
        n = len(arr)
        # Build a MAX_HEAP.
        for i in range(n, -1, -1):  # start from the last parent node
            self.heapify(arr, n, i) # heapify the tree
            #print("max heap",arr)
        # Swap nodes with root to sort
        for i in range(n-1, 0, -1): # start from the last node
            arr[i], arr[0] = arr[0], arr[i] # swap
            self.heapify(arr, i, 0) # heapify the tree
            #print("sorted",arr)
        return arr

s=Sorting_Algorithms()
print(s.bubbleSort([56,89,45,78,12,36,47,63,25,37,2,69,48,57,11]))
print(s.selectionSort([56,89,45,78,12,36,47,63,25,37,2,69,48,57,11]))
print(s.insertionSort([56,89,45,78,12,36,47,63,25,37,2,69,48,57,11]))
print(s.mergeSort([56,89,45,78,12,36,47,63,25,37,2,69,48,57,11]))
print(s.quickSort([56,89,45,78,12,36,47,63,25,37,2,69,48,57,11]))
print(s.heapSort([56,89,45,78,12,36,47,63,25,37,2,69,48,57,11]))
