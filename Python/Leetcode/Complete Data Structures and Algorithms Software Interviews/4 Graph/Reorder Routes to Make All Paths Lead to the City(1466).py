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


        