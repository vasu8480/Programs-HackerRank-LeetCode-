class Solution:
    def countBits(self, n):
        def b(n):
            return len([i for i in (bin(n)[2:]) if i!='0'])#counts the number of 1's in the binary representation of n
        return ([b(i) for i in range(n+1)]) 
print(Solution().countBits(5))
#-----------------------------------------------------------
class Solution:
    def countBits(self, n):
        return [bin(i).count('1') for i in range(n + 1)]
print(Solution().countBits(5))
#-----------------------------------------------------------
class Solution:
    def countBits(self, n):
        return [sum([int(x) for x in bin(i)[2:]]) for i in range(n + 1)]
print(Solution().countBits(5))
#-----------------------------------------------------------
class Solution:
    def countBits(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp
print(Solution().countBits(5))
#-----------------------------------------------------------