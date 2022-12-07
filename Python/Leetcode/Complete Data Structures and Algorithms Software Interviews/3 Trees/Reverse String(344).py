from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseRecursive(s, 0, len(s)-1)
        
    def reverseRecursive(self,s:List[str], start:int,end:int):
        if start > end:
            return
        (s[start],s[end]) = (s[end],s[start])
        self.reverseRecursive(s,start+1,end-1)

s=Solution()
l=["h","e","l","l","o"]
print(s.reverseString(l))
print(l)