'''
Created on Jul 13, 2017

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
class linkedlist(object):
    def __init__(self,head = None):
        self.head = head 
    def add(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.get_next()
        return count
    def search(self,data):
        current = self.head
        while current:
            if(current.get_data() == data):
                return True
            else:
                current = current.get_next()
        return False
    def insert(self,data,p):
        current = self.head
        count = 1
        while current:
            if(count == p):
                k = Node(data)
                p = current.get_next()
                current.set_next(k)
                k.set_next(p)
            else:
                count = count + 1
                current = current.get_next()  
    def list_print(self):
        node = self.head
        while node:
            print(node.data,end = ' ')
            node = node.next_node
l = linkedlist()
l.add(2)
l.add(3)
l.add(6)
l.insert(7,1)
print(l.list_print())