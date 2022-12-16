class Solution:
    def sumOfUnique(self, nums):
        return sum([i for i in nums if nums.count(i)==1])
print(Solution().sumOfUnique([1,2,3,2]))
#-----------------------------------------------------------
class Solution:
    def sumOfUnique(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return sum(i for i in d if d[i] == 1)
print(Solution().sumOfUnique([1,2,3,2]))
#-----------------------------------------------------------
class Solution:
    def sumOfUnique(self, nums):
        return sum(i for i in set(nums) if nums.count(i) == 1)
print(Solution().sumOfUnique([1,2,3,2]))