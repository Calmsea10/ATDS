#!/usr/bin/python3

class Stack(object):
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack)-1]
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.size()==0
    
class Queue(object):
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.size()==0

class Deque(object):
    def __init__(self):
        self.deque=[]
    
    def add_front(self,object):
        self.deque.insert(0,object)
    
    def add_rear(self,object):
        self.deque.append(object)
    
    def remove_front(self):
        return self.deque.pop(0)
    
    def remove_rear(self):
        return self.deque.pop()
    
    def size(self):
        return len(self.deque)
    
    def is_empty(self):
        return self.size()==0