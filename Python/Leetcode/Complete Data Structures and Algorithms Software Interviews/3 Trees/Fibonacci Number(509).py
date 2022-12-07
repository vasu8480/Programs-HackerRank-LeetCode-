class Solution:
    #Recursive
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
    #Iterative
    def fib(self, n: int) -> int:
        x,y=0,1 # time complexity is O(n) and space complexity is O(1)
        for i in range(n):
            x,y=y,x+y
        return x
    #Memoization
    def fib(self, n: int) -> int:
        memo={} # time complexity is O(n) and space complexity is O(n)
        def helper(n):
            if n in memo:
                return memo[n]
            if n<=1:
                return n
            memo[n]=helper(n-1)+helper(n-2)
            return memo[n]
        return helper(n)
print(Solution().fib(5))