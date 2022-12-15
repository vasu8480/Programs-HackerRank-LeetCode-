class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ""
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0   # string to int
            b = int(num2[j]) if j >= 0 else 0   # string to int
            i -= 1 
            j -= 1
            total = a + b + carry   # total = 3+6+0 = 9
            carry = 1 if total > 9 else 0   # carry = 0 #carry, total = divmod(a + b + carry, 10)
            result += str(total % 10)   # result = "9"  #   result += str(val)
        if carry:   # if carry>0
            result += "1"   
        return result[::-1 ]
print(Solution().addStrings("123", "456"))
print(Solution().addStrings("456","77"))
#-------------------------------------------------------------------------------------------------------
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry, res = 0, ""
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0:
            a = ord(num1[i]) - ord('0') if i >= 0 else 0    #ord('0') = 48 ord('1') = 49
            b = ord(num2[j]) - ord('0') if j >= 0 else 0
            carry, val = divmod(a + b + carry, 10)  # divmod(3+6+0, 10) = (0, 9)
            res += str(val)  # res = "9"
            i, j = i - 1, j - 1
        return (res + str(carry) if carry else res)[::-1]   
print(Solution().addStrings("123", "456"))
print(Solution().addStrings("456","77"))    