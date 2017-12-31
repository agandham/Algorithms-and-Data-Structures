'''
Created on Aug 7, 2017

@author: Abhilash Gandham
'''
class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbour(self,nbr,cost=0):
        self.connectedTo[nbr] = cost
    def getConnections(self):
        return self.connectedTo
class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.numvertices = 0
        self.A = []
        self.y = []
    def addVertex(self,key):
        newvertex = Vertex(key)
        self.vertices[key] = newvertex
        return newvertex
    def addEdge(self,f,n,cost=0):
        if f not in self.vertices:
            self.addVertex(f)
        if n not in self.vertices:
            self.addVertex(n)
        self.vertices[f].addNeighbour(n,cost)
    def print_edges(self):
        for i in self.vertices:
            for j in self.vertices[i].getConnections():
                print(i,j)
    def search(self,a,b):
        self.A.append(a)
        while(b  not in self.vertices[self.A[0]].getConnections()):
            for x in self.vertices[self.A[0]].getConnections():
                self.A.append(x)
#             print(self.A)
            self.y.append(self.A[0])
            del self.A[0]
#             print(self.A)
        else:
            self.y = self.y + self.A
            return self.y
                
g = Graph()
g.addVertex(2)
g.addVertex(3)
g.addEdge(2,3,11)
g.addEdge(2,4,14)
g.addEdge(3,6,11)
g.addEdge(6,5,12)
g.addEdge(4,7,11)
g.addEdge(7,5,12)
g.addEdge(2,8,12)
g.addEdge(8,9,11)
g.addEdge(9,5,11)
g.addEdge(8,16,11)
g.addEdge(16,5,11)
# g.print_edges()
x = g.search(2,5)
print(x)  
                    
        