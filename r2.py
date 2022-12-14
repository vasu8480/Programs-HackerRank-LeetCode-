if len(nums) == 1:
            return nums
        midPoint = int(len(nums)/2) 
        leftPart = nums[:midPoint]
        rightPart = nums[midPoint:] 
        return self.merge(self.merge(leftPart), self.merge(rightPart))
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