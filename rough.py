import collections


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        print(graph)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(-u)
        return self.dfs(graph, 0, set())

a=[[0,1],[1,3],[2,3],[4,0],[4,5]]
graph = collections.defaultdict(list)