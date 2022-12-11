class Solution:
    def leastBricks(self, wall):
        m = {} # key: ix , value -> number of gaps
        for row in wall:
            gapCount = 0
            for brick in row[:-1]: #not including the far right index
                gapCount += brick
                m[gapCount] = 1 + m.get(gapCount,0)
        return len(wall) - max(m.values()) if m else len(wall) #runtime is less than O(n^2) when compared to below
        #return len(wall) - max(m.values()) #runtime is more when compared to above
print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
#-----------------------------------------------------------------------------------------
from collections import Counter
class Solution:
    def leastBricks(self, wall):
        cnt = Counter()
        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                cnt[pos] += 1
        return len(wall) - cnt.most_common(1)[0][1] if cnt else len(wall)
print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
