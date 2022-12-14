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