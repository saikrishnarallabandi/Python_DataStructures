#!/usr/bin/python

# This is the library function for stack
'''
The functionalities provided to the user are:

a = Stack
a.push(A)
a.pop()
a.peek()
a.size()
a.isempty()

'''

class Stack:

 def __init__(self):
      self.items= []

 def isempty(self):
	  return self.items == []

 def push(self, elem):
      self.items.append(elem)      

 def pop(self):
	  return self.items.pop()

 def size(self):
	return len(self.items)

 def peek(self):
 	if len(self.items) == 0:
 		 print "No items in stack"
        else:
                 return self.items[len(self.items)-1]	  
