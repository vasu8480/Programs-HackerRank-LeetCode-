# File: BoyerMoore(169).py
from typing import List
import collections

#leetcode(169)
'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
#boyer-moore algorithm for O(1) space

def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if count == 0:
                result = num
            count += 1 if num == result else -1
        return result
print(majorityElement(1,[2,2,1,1,1,2,2]))

#--------------------------------------------------------------------
def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result = 0
        maxCount = 0

        for num in nums:
            count[num] = 1 + count.get(num,0)
            if count[num] > maxCount:
                result = num
            maxCount = max(maxCount,count[num])
        return result
print(majorityElement(1,[2,2,1,1,1,2,2]))
#------------------------------------------------------------

def majorityElement(self, nums: List[int]) -> int:
    a = collections.Counter(nums)
    return a.most_common(1)[0][0]

print(majorityElement(1,[2,2,1,1,1,2,2]))
# File: baseballscore(682).py
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
# File: Daily Temperatures(739).py
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

# File: Find the Duplicate Number(287).py
def findDuplicate(nums):
        slowPointer = 0 #time: O(n) space: O(1)
        fastPointer = 0 
        while True: 
            slowPointer = nums[slowPointer] #move slowPointer by 1
            fastPointer = nums[nums[fastPointer]] #move fastPointer by 2
            if slowPointer == fastPointer:
                break
        
        secondSlowPointer = 0
        
        while True:
            slowPointer = nums[slowPointer] #move slowPointer by 1 
            secondSlowPointer = nums[secondSlowPointer] #move secondSlowPointer by 1
            if slowPointer == secondSlowPointer:
                return slowPointer

nums=[3,1,2,5,8,7,9,4,6,8]
print(findDuplicate(nums))
#-------------------------------------------------------------------------------------------------------------
import collections #time complexity O(n) space complexity O(n)
nums=[3,1,3,4,2]
k=collections.Counter(nums)
print(k.most_common(1)[0][0])

#-------------------------------------------------------------------------------------------------------------
#O(n^2) --- Time Limit Exceeded
for i in range(0,len(nums)):
	for j in range(0,len(nums)):
		if i == j:
			continue
		if nums[i] == nums[j]:
			return nums[i]
				
# File: Intersection of 2 LL.py
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l = headA
        r = headB
        while l != r:
            l = l.next if l != None else headB
            r = r.next if r != None else headA
        return l
# File: removeNthFromEnd(19).py
class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        leftPointer = head
        rightPointer = head
        
        while n > 0 and rightPointer: #there is n gap between two pointers
            rightPointer = rightPointer.next
            n -= 1
        
        while rightPointer and rightPointer.next:  # stop when rightPointer.next is None.
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next
                
        if leftPointer == head and not rightPointer: #if we omit this, it won't work on the edge case of one node
            return head.next

        leftPointer.next = leftPointer.next.next #skip the leftPointer.next so it would be out of LinkedList
        
        return head
print(Solution().removeNthFromEnd([1,2,3,4,5], 2))
# File: Redundant Connection(684).py
class Solution:
    def findRedundantConnection(self, edges): # Union Find
        parents = []
        
        for i in range(len(edges) + 1):
            parents.append(i)

        ranks = [1] * (len(edges) + 1)
        
        def find(n):
            parent = parents[n] # find the root of the tree
            while parent != parents[parent]:
              #path compression to reduce the time complexity from O(n) to O(1)
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            return parent
        
        def union(n1, n2): # union by rank
            parent1, parent2 = find(n1), find(n2)
            
            if parent1 == parent2:
                return False
            
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
                ranks[parent1] += ranks[parent2]
            else:
                parents[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]
s=Solution()
print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
#---------------------------------------------------------------------------------------------------

class Solution:
    def findRedundantConnection(self, edges): # Union Find
        def find(x): 
            if x != parent[x]:
                parent[x] = find(parent[parent[x]]) # use this instead of parent[x] = find(parent[x]) to reduce the time complexity from O(n) to O(1)
               #parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        parent = [i for i in range(len(edges)+1)]
        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            union(edge[0], edge[1])
        return []

s=Solution()
print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))

# File: Reorder Routes to Make All Paths Lead to the City(1466).py
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set() 
        for a,b in connections:
            edges.add((a,b))
        
        neighbours = {}
        for city in range(n):
            neighbours[city] = []
        visited = set()
        counter = 0
        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
            
        def dfs(city): 
            nonlocal edges, neighbours, visited, counter
            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue  
                if (neighbour, city) not in edges:
                    counter += 1
                visited.add(neighbour)
                dfs(neighbour)
        visited.add(0)
        dfs(0)
        return counter
    
#-----------------------------------------------------------
import collections
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(-u)
        return self.dfs(graph, 0, set())

    def dfs(self, graph, node, visited): #time: O(V+E), space: O(V+E)
        visited.add(node)
        ans = 0
        for i in graph[node]:
            if i not in visited:
                ans += self.dfs(graph, abs(i), visited)
                if i > 0:
                    ans += 1
        return ans


        
# File: Binary Tree Maximum Path Sum(124).py
class Solution:
    answer = -float("inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.answer
    
    def dfs(self,node): #time: O(n), space: O(n)
        if node is None:
            return 0
        
        left = self.dfs(node.left) 
        right = self.dfs(node.right)
        
        left = max(left,0)
        right = max(right,0)
        
        self.answer = max(self.answer,node.val+left+right)
        
        return node.val + max(left,right)
#-------------------------------------------------------------
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') 
        self.dfs(root)
        return self.max_sum

    def dfs(self, node): #time: O(n), space: O(n)
        if not node:
            return 0
        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)
        self.max_sum = max(self.max_sum, node.val + left + right)
        return node.val + max(left, right)


# File: Convert BST to Greater Tree(538).py
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node): #time: O(n), space: O(n)
            if not node:
                return 0
            dfs(node.right)
            node.val += dfs.sum
            dfs.sum = node.val
            dfs(node.left)
            
        dfs.sum = 0
        dfs(root)
        return root
#--------------------------------------------------------------
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumOfValues = 0
        def traversal(node): #time: O(n), space: O(n)
            if not node:
                return
            nonlocal sumOfValues

            traversal(node.right)

            temp = node.val
            node.val += sumOfValues
            sumOfValues += temp
            
            traversal(node.left)

        traversal(root)
        return root
# File: Fibonacci Number(509).py
class Solution:
    #Recursive
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
    #Iterative
    def fib(self, n: int) -> int:
        x,y=0,1 # time complexity is O(n) and space complexity is O(1)
        for i in range(n):
            x,y=y,x+y
        return x
    #Memoization
    def fib(self, n: int) -> int:
        memo={} # time complexity is O(n) and space complexity is O(n)
        def helper(n):
            if n in memo:
                return memo[n]
            if n<=1:
                return n
            memo[n]=helper(n-1)+helper(n-2)
            return memo[n]
        return helper(n)
print(Solution().fib(5))
# File: Invert Binary Tree(226).py
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Exit condition
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
			
#------------------------------------------------------------#
class Solution:
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
			if root is None:
				return None
			else:
				root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
				return root
# File: Reverse String(344).py
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseRecursive(s, 0, len(s)-1)
        
    def reverseRecursive(self,s:List[str], start:int,end:int):
        if start > end:
            return
        (s[start],s[end]) = (s[end],s[start])
        self.reverseRecursive(s,start+1,end-1)
s=Solution()
l=["h","e","l","l","o"]
print(s.reverseString(l))
print(l)
# File: Brick Wall(554).py
class Solution:
    def leastBricks(self, wall):
        m = {} # key: ix , value -> number of gaps
        for row in wall:
            gapCount = 0
            for brick in row[:-1]: #not including the far right index
                gapCount += brick
                m[gapCount] = 1 + m.get(gapCount,0)
        return len(wall) - max(m.values()) if m else len(wall) #runtime is less than O(n^2) when compared to below
        #return len(wall) - max(m.values()) #runtime is more when compared to above
print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
#-----------------------------------------------------------------------------------------
from collections import Counter
class Solution:
    def leastBricks(self, wall):
        cnt = Counter()
        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                cnt[pos] += 1
        return len(wall) - cnt.most_common(1)[0][1] if cnt else len(wall)
print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))

# File: Encode and Decode TinyURL(535).py
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl
    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl
codec=Codec()
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))
print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))
#--------------------------------------------------------------------------------------------------------------
class Codec:
    def __init__(self):
        self.encodingMap = {}
        self.decodingMap = {}
        self.baseUrl = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodingMap:
            shortUrl = self.baseUrl + str(len(self.encodingMap) + 1)
            self.encodingMap[longUrl] = shortUrl
            self.decodingMap[shortUrl] = longUrl
        return self.encodingMap[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.decodingMap[shortUrl]
codec=Codec()
print(codec.decode(codec.encode("http://nurukurthivasu.tk")))
print(codec.encode("http://nurukurthivasu.tk"))
print(codec.decode('https://tinyurl.com/1'))

# File: Two Sum(1).py
class Solution:
    def twoSum(self, nums, target):
        m = {}
        n = len(nums)
        for i in range(0,n):
            goal = target - nums[i]
            if(goal in m):
                return [m[goal], i]
            m[nums[i]] = i
print(Solution().twoSum([2, 7, 11, 15], 9))
#---------------------------------------------------
class Solution:
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
print(Solution().twoSum([2, 7, 11, 15], 9))

# File: Find Median from Data Stream(295).py
import heapq 
class MedianFinder:
    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num) # because there is no maxHeap in python
        #small numbers in small heap, large numbers in large heap
        if self.smallHeap and self.largeHeap  and (-1 * self.smallHeap[0]) > self.largeHeap[0]:# if the top of small heap is larger than the top of large heap
            value = -1 * heapq.heappop(self.smallHeap) # pop the top of small heap
            heapq.heappush(self.largeHeap, value) # push it to large heap
        # small heap and large heap are almost equal in size
        if len(self.smallHeap) > len(self.largeHeap) + 1: # if the size of small heap is larger than the size of large heap by more than 1  
            value = -1 * heapq.heappop(self.smallHeap)  # pop the top of small heap
            heapq.heappush(self.largeHeap,value)  # push it to large heap
        if len(self.largeHeap) > len(self.smallHeap) + 1: # if the size of large heap is larger than the size of small heap by more than 1
            value = heapq.heappop(self.largeHeap) # pop the top of large heap
            heapq.heappush(self.smallHeap,-1 * value) # push it to small heap
    def findMedian(self) -> float:  # return the median
        if len(self.smallHeap) > len(self.largeHeap): # if the size of small heap is larger than the size of large heap
            return -1 * self.smallHeap[0] # return the top of small heap
        if len(self.largeHeap) > len(self.smallHeap): # if the size of large heap is larger than the size of small heap
            return self.largeHeap[0]  # return the top of large heap  
        return (-1 * self.smallHeap[0] + self.largeHeap[0]) / 2 # if the size of small heap is equal to the size of large heap, return the average of the top of small heap and the top of large heap

m=MedianFinder()
m.addNum(5)
m.addNum(3)
print(m.findMedian())
m.addNum(7)
m.addNum(9)
print(m.findMedian())
#------------------------------------------------------------------------------------------------
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.count = 0
    def addNum(self, num):
        if self.count % 2 == 0:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        self.count += 1
    def findMedian(self):
        if self.count % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return self.min_heap[0]
m=MedianFinder()
m.addNum(5)
m.addNum(3)
print(m.findMedian())
m.addNum(7)
m.addNum(9)
print(m.findMedian())
#------------------------------------------------------------------------------------------------
class MedianFinder:
    def __init__(self):
        self.nums = []
    def addNum(self, num):
        self.nums.append(num)
    def findMedian(self):
        self.nums.sort()
        if len(self.nums) % 2 == 0:
            return (self.nums[len(self.nums) // 2] + self.nums[len(self.nums) // 2 - 1]) / 2.0
        else:
            return self.nums[len(self.nums) // 2]
m=MedianFinder()
m.addNum(5)
m.addNum(3)
print(m.findMedian())
m.addNum(7)
m.addNum(9)
print(m.findMedian())
# File: K Closest Points to Origin(973).py
class Solution:
    def kClosest(self, points, k):
        points.sort(key=lambda P: P[0]**2 + P[1]**2)    # sort the points based on the distance from the origin 
        #for 3,3 it is 18 and for 5,-1 it is 26  and for -2,4 it is 20 sorted as [3,3] [-2,4] [5,-1]
        return points[:k]
print(Solution().kClosest([[3,3],[5,-1],[-2,4]],2))
#--------------------------------------------------------------------------------------------
import heapq
class Solution:
    def kClosest(self, points, k):
        minHeap = []
        for x,y in points:
            distanceToOrigin = (x**2) + (y**2) #do not have to take sqrt because we will compare anyway
            minHeap.append([distanceToOrigin,x,y]) #append distance as first element
        heapq.heapify(minHeap)  #heapify the list means it will be sorted by the first element of the list
        #print(minHeap)#[[18, 3, 3], [26, 5, -1], [20, -2, 4]]
        result = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap) #pop the first element of the list
            result.append([x,y])  #append the x and y coordinates
            k -= 1
        return result 
print(Solution().kClosest([[3,3],[5,-1],[-2,4]],2))
#---------------------------------------------------------------------------------------------
import heapq
class Solution:
    def kClosest(self, points, k):
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            if len(heap) < k:
                heapq.heappush(heap, (-dist, x, y)) #push the distance as negative because we want to sort in descending order
            else:
                heapq.heappushpop(heap, (-dist, x, y))  #push the distance as negative because we want to sort in descending order
                
        return [[x, y] for dist, x, y in heap]  #return the x and y coordinates
print(Solution().kClosest([[3,3],[5,-1],[-2,4]],2))
#-------------------------------------------------------------------------------------------------
class Solution:
    def kClosest(self, points, k):
        #merge sort
        def divideAndConquer(points):
            if len(points) == 1:
                return points
            mid = len(points) // 2
            left = divideAndConquer(points[:mid])
            right = divideAndConquer(points[mid:])
            return merge(left, right)
        def merge(left, right):
            i = j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i][0]**2 + left[i][1]**2 < right[j][0]**2 + right[j][1]**2:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result
        return divideAndConquer(points)[:k]
print(Solution().kClosest([[3,3],[5,-1],[-2,4]],2))
