class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+':
            sign = s[0]
            s = s[1:]
        else:
            sign = '+'
        res = 0
        for i in range(len(s)):
            if s[i].isdigit():
                res = res*10 + int(s[i])
            else:
                break
        if sign == '-':
            res = -res
        if res > 2**31 - 1:
            return 2**31 - 1
        if res < -2**31:
            return -2**31
        return res
s=Solution()
print(s.myAtoi("42"))
print(s.myAtoi("   -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("3.14159"))
print(s.myAtoi("+-2"))
print(s.myAtoi("  -0012a42"))
print(s.myAtoi("  +0 123"))
