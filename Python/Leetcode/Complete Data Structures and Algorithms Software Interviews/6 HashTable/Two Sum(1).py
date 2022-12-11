class Solution:
    def twoSum(self, nums, target):
        m = {}
        n = len(nums)
        for i in range(0,n):
            goal = target - nums[i]
            if(goal in m):
                return [m[goal], i]
            m[nums[i]] = i
print(Solution().twoSum([2, 7, 11, 15], 9))
#---------------------------------------------------
class Solution:
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
print(Solution().twoSum([2, 7, 11, 15], 9))
