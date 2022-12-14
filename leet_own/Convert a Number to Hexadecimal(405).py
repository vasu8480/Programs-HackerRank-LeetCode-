class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 2 ** 32
        return hex(num)[2:]
print(Solution().toHex(26))
print(Solution().toHex(-1))
#------------------------------------------------------------
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        s = ''
        while num and len(s) < 8:
            s = '0123456789abcdef'[num & 15] + s
            num >>= 4
        return s
print(Solution().toHex(26))
