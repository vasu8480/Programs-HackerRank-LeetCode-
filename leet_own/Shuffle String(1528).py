class Solution:
    def restoreString(self, s: str, indices):
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)
print(Solution().restoreString('codeleet', [4,5,6,7,0,2,1,3]))
#--------------------------------------------------------------------
class Solution:
    def restoreString(self, s: str, indices):
        return ''.join([s[indices.index(i)] for i in range(len(s))])
print(Solution().restoreString('codeleet', [4,5,6,7,0,2,1,3]))