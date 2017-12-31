'''
Created on Jul 16, 2017

@author: Abhilash Gandham
'''
from __future__ import print_function
class Node(object):
    def __init__(self,data = None,next_node = None):
        self.data = data
        self.next_node = next_node 
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next
class LinkedList(object):
    def __init__(self):
        self.prev = None
        self.head = None
        self.x = None
    def add(self,data):
        if self.prev is None:
            new_node = Node(data)
            new_node.set_next(None)
            self.prev = new_node
            self.head = new_node
            self.x = new_node
        else:
            new_node1 = Node(data)
            new_node1.next_node = None
            self.prev.next_node = new_node1
            self.prev = new_node1
    def pop(self):
        while(self.head.next_node == self.prev):
            self.head.next_node = None
            self.prev = self.head
        else:
            self.head = self.head.next_node 
            self.x.next_node = None
    def pop_hope(self):
        while(self.head.next_node != self.prev):
            self.head = self.head.next_node
        else:
            self.head.next_node = None
            self.prev = self.head
        self.head = self.x
    def delete_node(self,data):
        if(self.head.data == data): 
            self.x = self.head.next_node
            self.head.next_node = None
        else:
            while(self.head.next_node.data != data):
                self.head = self.head.next_node
            else:
                self.head.next_node = self.head.next_node.next_node
        self.head = self.x    
    def print_list(self):
        while(self.head):
            print(self.head.get_data(),end = ' ')
            self.head = self.head.get_next()
l = LinkedList()
l.add(2)
l.add(3)
l.add(4)
l.add(7)
l.delete_node(3)
l.print_list()          