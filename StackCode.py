# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 09:36:56 2022

@author: Sanjay
"""

class Stack(object):
    
    def __init__(self):
        self.item = []
        
    def push(self, item = ''):
        # Pushing the element at last index
        self.item.append(item)
        
    def pop(self):
        # Poping the last elements/item
        # return: None
        self.item.pop()
        pass
    
    def peek(self):
        #Allow ys to see last element
        # return: last item
        if self.item:
            return self.item[-1]
        else:
            return None
        
    def size(self):
        # Tells the size of stack
        if self.item:
            return len(self.item)
        else:
            return None
        
    def isEmpty(self):
        # Tells if stack is empty
        if self.item == []:
            return True
        else:
            return False
        
if __name__ == "__main__":
    stack = Stack()
    stack.push('7')
    stack.push('4')
    print(stack.size())
    print(stack.peek())
    
    stack.pop()
    print(stack.size())
    print(stack.peek())
    
    print(stack.isEmpty())
    
    
    