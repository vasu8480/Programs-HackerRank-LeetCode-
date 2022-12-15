class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l = [start + 2 * i for i in range(n)]
        res = 0
        for i in l:
            res ^= i
        return res
print(Solution().xorOperation(5, 0))
#------------------------------------------------------------
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res
print(Solution().xorOperation(5, 0))
#------------------------------------------------------------
from functools import reduce
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda x, y: x ^ y, [start + 2 * i for i in range(n)])
print(Solution().xorOperation(5, 0))