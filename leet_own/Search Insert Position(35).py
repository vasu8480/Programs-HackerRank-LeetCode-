class Solution:
    def searchInsert(self, nums,target):
        for i in range(len(nums)):
            if target==nums[i] or target<nums[i]:
                return i
        return len(nums)
print(Solution().searchInsert([1,3,5,6], 5))
#---------------------------------------------------------
class Solution:
    def searchInsert(self, nums,target):
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
#---------------------------------------------------------
print(Solution().searchInsert([1,3,5,6], 5))
class Solution:
    def searchInsert(self, nums,target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
print(Solution().searchInsert([1,3,5,6], 5))
#---------------------------------------------------------
class Solution:
    def searchInsert(self, nums,target):
        return len([x for x in nums if x < target])
print(Solution().searchInsert([1,3,5,6], 5))