'''
Created on Jul 16, 2017

@author: Abhilash Gandham
'''
from __future__ import print_function
class Node(object):
    def __init__(self,data,prev_node = None,next_node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node 
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def get_prev(self):
        return self.prev_node
    def set_next(self,new_next):
        self.next_node = new_next
    def set_prev(self,new_prev):
        self.prev_node = new_prev
class DoubleLinkedList(object):
    def __init__(self,prev = None):
        self.prev = None
        self.head = None
    def add(self,data):
        if self.prev is None:
            new_node = Node(data)
            self.prev = new_node
            self.head = new_node
        else:
            new_node1 = Node(data)
            new_node1.set_prev(self.prev)
            self.prev.next_node = new_node1
            self.prev = new_node1
    def print_list(self):
        while(self.head):
            print(self.head.get_data(),end = ' ')
            self.head = self.head.get_next()
l1 = DoubleLinkedList()
l1.add(2)
l1.add(3)
l1.add(4)
l1.print_list()