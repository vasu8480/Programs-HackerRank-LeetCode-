class Solution:
    def thirdMax(self, nums):
        nums=list(set(nums))
        nums.sort()
        for i in range(1):
            if len(nums) >2:
                return (nums[-3])
            else:
                return (nums[-1])
print(Solution().thirdMax([3,2,1]))
print(Solution().thirdMax([1,2]))
#--------------------------------------------------
class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            nums.sort()
            return nums[-3]
print(Solution().thirdMax([3,2,1]))
#---------------------------------------------------
class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
print(Solution().thirdMax([3,2,1]))
print(Solution().thirdMax([1,2]))