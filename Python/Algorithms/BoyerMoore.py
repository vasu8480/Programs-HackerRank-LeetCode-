from typing import List
import collections

#leetcode(169)
'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
#boyer-moore algorithm for O(1) space

def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if count == 0:
                result = num
            count += 1 if num == result else -1
        return result
print(majorityElement(1,[2,2,1,1,1,2,2]))

#--------------------------------------------------------------------
def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result = 0
        maxCount = 0

        for num in nums:
            count[num] = 1 + count.get(num,0)
            if count[num] > maxCount:
                result = num
            maxCount = max(maxCount,count[num])
        return result
print(majorityElement(1,[2,2,1,1,1,2,2]))
#------------------------------------------------------------

def majorityElement(self, nums: List[int]) -> int:
    a = collections.Counter(nums)
    return a.most_common(1)[0][0]

print(majorityElement(1,[2,2,1,1,1,2,2]))