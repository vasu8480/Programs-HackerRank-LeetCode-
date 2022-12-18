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