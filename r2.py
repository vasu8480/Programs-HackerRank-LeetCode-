class Solution:
    def productExceptSelf(self, nums):
        # 1. calculate the product of all numbers
        # 2. divide the product by each number
        # 3. return the list of products
        product = 1
        for num in nums:
            product *= num
        return [product/num for num in nums]
print(Solution().productExceptSelf([1,2,3,4]))
#--------------------------------------------------------------------------------
class Solution:
    def productExceptSelf(self, nums):
        # 1. calculate the product of all numbers
        # 2. divide the product by each number
        # 3. return the list of products
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            nums[i] = product
        product = 1
        for i in range(len(nums)-1, -1, -1):
            nums[i] = nums[i-1] * product if i > 0 else product
            product *= nums[i]
        return nums
print(Solution().productExceptSelf([1,2,3,4]))