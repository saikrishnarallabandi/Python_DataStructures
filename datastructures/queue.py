#!/usr/bin/python

# This is the library function for queue
'''
The functionalities provided to the user are:

a = Queue
a.enqueue(A)
a.dequeue()
a.size()
a.isempty()

'''

class Queue:

    def __init__(self):
		self.items = []

    def isempty(self):
	    return self.items == []

    def enqueue(self,elem):
	    self.items.insert(0, elem)

    def dequeue(self):
	    return self.items.pop()

    def size(self):
    	return len(self.items)

