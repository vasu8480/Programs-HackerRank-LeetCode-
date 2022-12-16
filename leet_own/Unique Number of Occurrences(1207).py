class Solution:
    def uniqueOccurrences(self, arr):
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return len(d.values()) == len(set(d.values()))
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
#--------------------------------------------------------------
import collections
class Solution:
    def uniqueOccurrences(self, arr):
        a = collections.Counter(arr)
        return len(a) == len(set(a.values()))
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
#-------------------------------------------------------------- 
class Solution:
    def uniqueOccurrences(self, arr):
        return len(set(arr.count(i) for i in arr)) == len(set(arr))
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))

