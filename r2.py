class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ""
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            print(a, b, carry)
            i -= 1
            j -= 1
            total = a + b + carry
            carry = 1 if total > 9 else 0
            result += str(total % 10)
            print(result)
        if carry:
            result += "1"
        return result[::-1 ]
print(Solution().addStrings("123", "456"))
#--------------------------------------------------
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry, res = 0, ""
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0:
            a = ord(num1[i]) - ord('0') if i >= 0 else 0
            b = ord(num2[j]) - ord('0') if j >= 0 else 0
            carry, val = divmod(a + b + carry, 10)
            res += str(val)
            i, j = i - 1, j - 1
        return res + str(carry) if carry else res[::-1]
print(Solution().addStrings("123", "456"))