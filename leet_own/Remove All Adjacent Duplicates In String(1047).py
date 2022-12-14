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
