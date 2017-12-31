'''
Created on Aug 5, 2017

@author: Abhilash Gandham
'''
import sys
class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None

    def get_id(self):
        return self.__id


    def get_connected_to(self):
        return self.__connectedTo


    def get_color(self):
        return self.__color


    def get_dist(self):
        return self.__dist


    def get_pred(self):
        return self.__pred


    def set_id(self, value):
        self.__id = value


    def set_connected_to(self, value):
        self.__connectedTo = value


    def set_color(self, value):
        self.__color = value


    def set_dist(self, value):
        self.__dist = value


    def set_pred(self, value):
        self.__pred = value


    def del_id(self):
        del self.__id


    def del_connected_to(self):
        del self.__connectedTo


    def del_color(self):
        del self.__color


    def del_dist(self):
        del self.__dist


    def del_pred(self):
        del self.__pred

    def addNeighbour(self,nbr,cost=0):
        self.connectedTo[nbr] = cost
    def getConnections(self):
        return self.connectedTo
class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.numvertices = 0
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
g = Graph()
g.addVertex(2)
g.addVertex(3)
g.addEdge(2,3,11)
g.addEdge(4,5,12)
g.addEdge(2,4,14)
g.print_edges()            
                    
        