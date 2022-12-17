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
