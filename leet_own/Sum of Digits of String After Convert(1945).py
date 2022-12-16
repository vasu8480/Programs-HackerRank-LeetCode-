class Solution:
    def getLucky(self, s: str, k: int) -> int:
        orf= lambda i: ord(i) - 97
        def convert(s,k):
            m=""
            for i in s:
                m += str(orf(i)+1)
            s=sum(int(i) for i in m)
            while k>1:
                k-=1
                s=sum(int(i) for i in str(s))
            return s
        return convert(s,k)
print(Solution().getLucky('leetcode', 2))
#------------------------------------------------------------------
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join([str(ord(c)-96) for c in s])
        for _ in range(k):
            s = str(sum([int(c) for c in s]))
        return int(s)
print(Solution().getLucky('leetcode', 2))