class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
print(Solution().findTheDifference('abcd', 'abcde'))
#----------------------------------------------------------------
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in s:
            t = t.replace(c, '', 1) # replace() returns a copy of the string with all occurrences of substring old replaced by new. If the optional argument max is given, only the first count occurrences are replaced.
        return t
print(Solution().findTheDifference('abcd', 'abcde'))
#----------------------------------------------------------------
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s))) # ord() returns the unicode code point for a one-character string
print(Solution().findTheDifference('abcd', 'abcde'))
