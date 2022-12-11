def findDuplicate(nums):
        slowPointer = 0 #time: O(n) space: O(1)
        fastPointer = 0 
        while True: 
            slowPointer = nums[slowPointer] #move slowPointer by 1
            fastPointer = nums[nums[fastPointer]] #move fastPointer by 2
            if slowPointer == fastPointer:
                break
        
        secondSlowPointer = 0
        
        while True:
            slowPointer = nums[slowPointer] #move slowPointer by 1 
            secondSlowPointer = nums[secondSlowPointer] #move secondSlowPointer by 1
            if slowPointer == secondSlowPointer:
                return slowPointer

nums=[3,1,2,5,8,7,9,4,6,8]
print(findDuplicate(nums))
#-------------------------------------------------------------------------------------------------------------
import collections #time complexity O(n) space complexity O(n)
nums=[3,1,3,4,2]
k=collections.Counter(nums)
print(k.most_common(1)[0][0])

#-------------------------------------------------------------------------------------------------------------
#O(n^2) --- Time Limit Exceeded
for i in range(0,len(nums)):
	for j in range(0,len(nums)):
		if i == j:
			continue
		if nums[i] == nums[j]:
			return nums[i]
				