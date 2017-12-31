'''
Created on Aug 9, 2017

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
    def dsearch(self,b):
        for i in self.vertices:
            self.sear(i,b)
        return self.A
    def sear(self,a,b):
        for i in self.vertices[a].getConnections():
                self.A.append(i)
                self.sear(i,b)
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
x = g.dsearch(5)
print(x)
                
                