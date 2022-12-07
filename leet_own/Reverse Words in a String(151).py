class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        
print(Solution().fib("the sky is blue"))