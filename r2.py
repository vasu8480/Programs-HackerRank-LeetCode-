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