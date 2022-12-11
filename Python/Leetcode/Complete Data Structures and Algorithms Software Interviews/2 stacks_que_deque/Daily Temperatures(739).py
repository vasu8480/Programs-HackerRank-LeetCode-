from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # initialize with 0s so we don't have to manually add 0s if none is compliant later on
        stack = [] #storing pair of temperature and corresponding index 
        for i, v in enumerate(temperatures):
            while stack and v > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
print(Solution().dailyTemperatures( [73,74,75,71,69,72,76,73]))

#--------------------------------------------------------------------------------
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # initialize with 0s so we don't have to manually add 0s if none is compliant later on
        stack = [] #storing pair of temperature and corresponding index 
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]: # if the current temperature is greater than the last temperature in the stack
                stackTemperature, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([v, i])
        return result
print(Solution().dailyTemperatures( [73,74,75,71,69,72,76,73]))
