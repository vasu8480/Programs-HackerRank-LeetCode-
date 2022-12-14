class Solution:
    def removeDuplicates(self, s: str) -> str:
        k=""
        for i in range(len(s)):
            if k=="":
                k=k+s[i]
            elif k[-1]==s[i]:
                k=k[:-1]
            else:
                k=k+s[i]
        return k
print(Solution().removeDuplicates("abbaca"))
#-------------------------------------------------
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
print(Solution().removeDuplicates("abbaca"))
