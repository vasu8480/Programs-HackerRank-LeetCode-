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
