from typing import List

def majorityElement(self, nums: List[int]) -> int:
    count = 0
    res = 0
    for num in nums:
        if count == 0:
            res = num
        count += 1 if num == res else -1
    return res

print(majorityElement(1,[2,2,1,1,1,2,2]))