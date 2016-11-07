#!/usr/bin/python

# This is the library function for dequeue
'''
The functionalities provided to the user are:

a = Dequeue
a.add_rear(A)
a.add_front(A)
a.remove_rear(A)
a.remove_front(A)
a.isempty()
a.size()

'''

class Dequeue:

    def __init__(self):
		self.items = []

    def isempty(self):
	    return self.items == []

    def size(self):
        return len(self.items)
 
    def add_front(self,elem):
	    self.items.append(elem)

    def add_rear(self, elem):
	    return self.items.insert(0, elem)

    def remove_front(self):
        self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

 
