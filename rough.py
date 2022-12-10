class Graph:
    def __init__(self):
        self.adjDict = {}

    def addVertex(self, vertex):
        if vertex not in self.adjDict.keys():
            self.adjDict[vertex] = []
            return True
        return False

    def addEdge(self, v1, v2):
        if v1 in self.adjDict.keys() and v2 in self.adjDict.keys():
            self.adjDict[v1].append(v2)
            self.adjDict[v2].append(v1)
            return True
        return False

    def removeEdge(self, v1, v2):
        if v1 in self.adjDict.keys() and v2 in self.adjDict.keys():
            try:
                self.adjDict[v1].remove(v2)
                self.adjDict[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjDict.keys():
            for relatedVertex in self.adjDict[vertex]:
                self.adjDict[relatedVertex].remove(vertex)
            del self.adjDict[vertex]
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adjDict:
            print(vertex, '->', self.adjDict[vertex]) 
myGraph = Graph()
myGraph.addVertex('A')
myGraph.addVertex('B')
myGraph.addVertex('C')
myGraph.addVertex('D')

myGraph.addEdge('A', 'B')   
myGraph.addEdge('A', 'C')
myGraph.addEdge('B', 'D')
myGraph.addEdge('C', 'D')
print(myGraph.adjDict)
myGraph.printGraph()

myGraph.removeEdge('A', 'B')
print(myGraph.adjDict)
myGraph.printGraph()
