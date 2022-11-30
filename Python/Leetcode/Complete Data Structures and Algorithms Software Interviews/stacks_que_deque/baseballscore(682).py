from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        # This is O(N) since we are iterating through
        # Since we are using lifo, stack is great but we can implement it with list as in this example
        
        l = []
        for op in ops:
            if op == "+":
                l.append(l[-1] + l[-2])
            elif op == "C":
                l.pop()
            elif op == "D":
                l.append(2 * l[-1])
            else:
                l.append(int(op))
        return sum(l)

print(Solution().calPoints(["5","2","C","D","+"]))