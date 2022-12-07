from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: #time complexity O(1) space complexity O(1)
            return nums[0]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]        
print(Solution().findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#-------------------------#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums) #time complexity O(n) space complexity O(1)        
print(Solution().findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))