# File: Add Strings(415).py
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
# File: Binary Search(704).py
class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
print(Solution().search([-1,0,3,5,9,12], 9))
# File: Bitwise AND of Numbers Range(201).py
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)
        return right

print(Solution().rangeBitwiseAnd(5,7))
# File: Convert a Number to Hexadecimal(405).py
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

# File: Counting Bits(338).py
class Solution:
    def countBits(self, n):
        def b(n):
            return len([i for i in (bin(n)[2:]) if i!='0'])#counts the number of 1's in the binary representation of n
        return ([b(i) for i in range(n+1)]) 
print(Solution().countBits(5))
#-----------------------------------------------------------
class Solution:
    def countBits(self, n):
        return [bin(i).count('1') for i in range(n + 1)]
print(Solution().countBits(5))
#-----------------------------------------------------------
class Solution:
    def countBits(self, n):
        return [sum([int(x) for x in bin(i)[2:]]) for i in range(n + 1)]
print(Solution().countBits(5))
#-----------------------------------------------------------
class Solution:
    def countBits(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp
print(Solution().countBits(5))
#-----------------------------------------------------------
# File: Find Minimum in Rotated Sorted Array II(154).py
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: #time complexity O(1) space complexity O(1)
            return nums[0]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]        
print(Solution().findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#-------------------------#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums) #time complexity O(n) space complexity O(1)        
print(Solution().findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# File: Find the Difference(389).py
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

# File: Fizz Buzz(412).py
class Solution:
    def fizzBuzz(self, n):
        l=[]
        for i in range(1,n+1):
            if i%15==0:
                l.append("FizzBuzz")
            elif i%3==0:
                l.append("Fizz")
            elif i%5==0:
                l.append("Buzz")
            else:
                l.append("{}".format(i))
        return l
print(Solution().fizzBuzz(15))
#-----------------------------------------------------------------------------------------------------------------------
class Solution:
    def fizzBuzz(self, n):
        return [str(i) if i % 3 and i % 5 else 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) for i in range(1, n + 1)]
print(Solution().fizzBuzz(15))
# File: Number of Days Between Two Dates(1360).py
import calendar
from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1=date1.split("-")
        d2=date2.split("-")
        da1=calendar.datetime.date(int(d1[0]),int(d1[1]),int(d1[2]))
        da2=calendar.datetime.date(int(d2[0]),int(d2[1]),int(d2[2]))
        return  abs((da2-da1).days)
print(Solution().daysBetweenDates("2020-01-15","2019-12-31"))
#-----------------------------------------------------------------------------
import calendar
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def get_days(date):
            y, m, d = map(int, date.split('-'))
            return calendar.timegm((y, m, d, 0, 0, 0))
        return abs(get_days(date1) - get_days(date2)) // (24 * 60 * 60)
print(Solution().daysBetweenDates("2020-01-15","2019-12-31"))
#-----------------------------------------------------------------------------
import calendar
from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((datetime.strptime(date1, '%Y-%m-%d') - datetime.strptime(date2, '%Y-%m-%d')).days)
print(Solution().daysBetweenDates("2020-01-15","2019-12-31"))


# File: Product of Array Except Self(238).py
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
print(Solution().productExceptSelf([1,2,3,4]))
# File: Remove All Adjacent Duplicates In String(1047).py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        k=""
        for i in range(len(s)):
            if k=="":   # if k is empty
                k=k+s[i]    # add the first element
            elif k[-1]==s[i]:  # if the last element of k is equal to the current element
                k=k[:-1]    # remove the last element of k
            else:   # if the last element of k is not equal to the current element
                k=k+s[i]    # add the current element to k
        return k
print(Solution().removeDuplicates("abbaca"))
#-------------------------------------------------
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []  # create an empty stack
        for c in s: # for each character in s
            if stack and stack[-1] == c:    # if the stack is not empty and the last element of the stack is equal to the current character
                stack.pop() # remove the last element of the stack
            else:   # if the stack is empty or the last element of the stack is not equal to the current character
                stack.append(c) # add the current character to the stack
        return ''.join(stack)
print(Solution().removeDuplicates("abbaca"))

# File: Reverse Bits(190).py
# run in leetcode run throws error: "TypeError: 'int' object is not subscriptable"
class Solution:
    def reverseBits(self, n: int) -> int:
        return int("{:032b}".format(n)[::-1], 2) #convert the number to binary, reverse it and convert it back to decimal
print(Solution().reverseBits(00000010100101000001111010011100))
#---------------------------------------------------------------------------------------------------class Solution:
def reverseBits(self, n: int) -> int:
    binary = "{:032b}".format(n) #convert the number to binary  
    reverse = binary[::-1] #reverse the binary number
    return int(reverse, 2) #convert the reversed binary number to decimal
print(Solution().reverseBits(00000010100101000001111010011100))
#---------------------------------------------------------------------------------------------------class Solution:
def reverseBits(self, n: int) -> int:
    binary = "{:032b}".format(n) #convert the number to binary  
    reverse = binary[::-1] #reverse the binary number
    decimal = 0
    for i in range(len(reverse)): #loop through the binary number
        if reverse[i] == "1": #if the current digit is 1
            decimal += 2 ** i #add 2^i to the decimal number
    return decimal #return the decimal number
print(Solution().reverseBits(00000010100101000001111010011100))
# File: Reverse Linked List(206).py
class Solution:
    root=None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None:
            return None
        if head.next==None:
            self.root=head
            return head
        self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return self.root

#------------------------------------------------------------
class Solution:
    root=None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while head:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev
# File: Reverse Words in a String(151).py
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        
print(Solution().fib("the sky is blue"))
# File: Search Insert Position(35).py
class Solution:
    def searchInsert(self, nums,target):
        for i in range(len(nums)):
            if target==nums[i] or target<nums[i]:
                return i
        return len(nums)
print(Solution().searchInsert([1,3,5,6], 5))
#---------------------------------------------------------
class Solution:
    def searchInsert(self, nums,target):
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
#---------------------------------------------------------
print(Solution().searchInsert([1,3,5,6], 5))
class Solution:
    def searchInsert(self, nums,target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
print(Solution().searchInsert([1,3,5,6], 5))
#---------------------------------------------------------
class Solution:
    def searchInsert(self, nums,target):
        return len([x for x in nums if x < target])
print(Solution().searchInsert([1,3,5,6], 5))
# File: Shuffle String(1528).py
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
# File: Sort the People(2481).py
from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        people.sort(key=lambda x: (-x[1], x[0]))
        return [name for name, height in people]
print(Solution().sortPeople(["Mary","John","Emma"],[180,165,170]))
#--------------------------------------------------------------
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [row[1] for row in sorted(zip(heights, names), reverse = True)]
print(Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
# File: String Matching in an Array(1408).py
class Solution:
    def stringMatching(self, words):
        l=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j] and words[i] not in l:
                    l.append(words[i])
                elif words[j] in words[i] and words[j] not in l:
                    l.append(words[j])
        return l
print(Solution().stringMatching(["mass","as","hero","superhero"]))
#---------------------------------------------------------------------------------
class Solution:
    def stringMatching(self, words):
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
print(Solution().stringMatching(["mass","as","hero","superhero"]))
#---------------------------------------------------------------------------------
class Solution:
    def stringMatching(self, words):
        return [word for word in words if any(word in w for w in words if w != word)]
print(Solution().stringMatching(["mass","as","hero","superhero"]))
#---------------------------------------------------------------------------------
class Solution:
    def stringMatching(self, words):
        return sorted({w for word in words for w in words if w != word and w in word})
# File: String to Integer (atoi)(8).py
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

# File: Sum of Digits of String After Convert(1945).py
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        orf= lambda i: ord(i) - 97
        def convert(s,k):
            m=""
            for i in s:
                m += str(orf(i)+1)
            s=sum(int(i) for i in m)
            while k>1:
                k-=1
                s=sum(int(i) for i in str(s))
            return s
        return convert(s,k)
print(Solution().getLucky('leetcode', 2))
#------------------------------------------------------------------
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join([str(ord(c)-96) for c in s])
        for _ in range(k):
            s = str(sum([int(c) for c in s]))
        return int(s)
print(Solution().getLucky('leetcode', 2))
# File: Sum of Unique Elements(1748).py
class Solution:
    def sumOfUnique(self, nums):
        return sum([i for i in nums if nums.count(i)==1])
print(Solution().sumOfUnique([1,2,3,2]))
#-----------------------------------------------------------
class Solution:
    def sumOfUnique(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return sum(i for i in d if d[i] == 1)
print(Solution().sumOfUnique([1,2,3,2]))
#-----------------------------------------------------------
class Solution:
    def sumOfUnique(self, nums):
        return sum(i for i in set(nums) if nums.count(i) == 1)
print(Solution().sumOfUnique([1,2,3,2]))
# File: Third Maximum Number(414).py
class Solution:
    def thirdMax(self, nums):
        nums=list(set(nums))
        nums.sort()
        for i in range(1):
            if len(nums) >2:
                return (nums[-3])
            else:
                return (nums[-1])
print(Solution().thirdMax([3,2,1]))
print(Solution().thirdMax([1,2]))
#--------------------------------------------------
class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            nums.sort()
            return nums[-3]
print(Solution().thirdMax([3,2,1]))
#---------------------------------------------------
class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
print(Solution().thirdMax([3,2,1]))
print(Solution().thirdMax([1,2]))
# File: Top K Frequent Elements(347).py
import collections
class Solution:
    def topKFrequent(self, nums, k):
        # 1. count the frequency of each number
        # 2. sort the numbers by frequency
        # 3. return the top k numbers
        count = collections.Counter(nums)
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
#--------------------------------------------------------------------------------
import collections
class Solution:
    def topKFrequent(self, nums,k):
        # 1. count the frequency of each number
        # 2. sort the numbers by frequency
        # 3. return the top k numbers
        count = collections.Counter(nums)
        return [i[0] for i in count.most_common(k)] # most_common() returns a list of tuples
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
#--------------------------------------------------------------------------------
import heapq
class Solution:
    def topKFrequent(self, nums,k):
        # 1. count the frequency of each number
        # 2. sort the numbers by frequency
        # 3. return the top k numbers
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get) # nlargest returns a list of keys
print(Solution().topKFrequent([1,1,1,2,2,3], 2))

# File: Unique Number of Occurrences(1207).py
class Solution:
    def uniqueOccurrences(self, arr):
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return len(d.values()) == len(set(d.values()))
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
#--------------------------------------------------------------
import collections
class Solution:
    def uniqueOccurrences(self, arr):
        a = collections.Counter(arr)
        return len(a) == len(set(a.values()))
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
#-------------------------------------------------------------- 
class Solution:
    def uniqueOccurrences(self, arr):
        return len(set(arr.count(i) for i in arr)) == len(set(arr))
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))


# File: XOR Operation in an Array(1486).py
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l = [start + 2 * i for i in range(n)]
        res = 0
        for i in l:
            res ^= i
        return res
print(Solution().xorOperation(5, 0))
#------------------------------------------------------------
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res
print(Solution().xorOperation(5, 0))
#------------------------------------------------------------
from functools import reduce
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda x, y: x ^ y, [start + 2 * i for i in range(n)])
print(Solution().xorOperation(5, 0))