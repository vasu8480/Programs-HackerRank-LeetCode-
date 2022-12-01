def findDuplicate(self, nums: List[int]) -> int:
        slowPointer = 0
        fastPointer = 0
        while True:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]
            if slowPointer == fastPointer:
                break
        
        secondSlowPointer = 0
        
        while True:
            slowPointer = nums[slowPointer]
            secondSlowPointer = nums[secondSlowPointer]
            if slowPointer == secondSlowPointer:
                return slowPointer
								