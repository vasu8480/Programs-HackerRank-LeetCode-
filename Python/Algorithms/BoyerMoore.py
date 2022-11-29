from typing import List
import collections
#BoyerMoore Algorithm
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    res = 0
    for num in nums:
        if count == 0:
            res = num
        count += 1 if num == res else -1
    return res

print(majorityElement(1,[2,2,1,1,1,2,2]))

#------------------------------------------------------------

def majorityElement(self, nums: List[int]) -> int:
    a = collections.Counter(nums)
    return a.most_common(1)[0][0]

print(majorityElement(1,[2,2,1,1,1,2,2]))