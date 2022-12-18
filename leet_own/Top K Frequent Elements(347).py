import collections
class Solution:
    def topKFrequent(self, nums, k):
        # 1. count the frequency of each number
        # 2. sort the numbers by frequency
        # 3. return the top k numbers
        count = collections.Counter(nums)
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
#--------------------------------------------------------------------------------
import collections
class Solution:
    def topKFrequent(self, nums,k):
        # 1. count the frequency of each number
        # 2. sort the numbers by frequency
        # 3. return the top k numbers
        count = collections.Counter(nums)
        return [i[0] for i in count.most_common(k)] # most_common() returns a list of tuples
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
#--------------------------------------------------------------------------------
import heapq
class Solution:
    def topKFrequent(self, nums,k):
        # 1. count the frequency of each number
        # 2. sort the numbers by frequency
        # 3. return the top k numbers
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get) # nlargest returns a list of keys
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
