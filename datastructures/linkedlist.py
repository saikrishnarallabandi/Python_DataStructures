#!/usr/bin/python

# This is the library function for linkedlist
'''
The functionalities provided to the user are:

a = LinkedList()
a.add(item)
a.remove(item)
a.is_empty()
a.size()

'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
	    return self.data

	def get_next(self):
	    return self.next

	def set_data(self, elem):
	    self.data = elem

	def set_next(self, val):
	    self.next = val            	

class LinkedList:
	
     def __init__(self):
		self.head = None

     def is_empty(self):
     	 return self.head == None

     def add(self, data):
          temp = Node(data)
          temp.set_next(self.head)
          self.head = temp
     
     def size(self):
          current = self.head
          count = 0

          while(current != None):
              count += 1
              current = current.get_next()              
          return count

     def search(self, elem):
           current = self.head
           found = False
           while(current != None and not found):
                 
                 if current.get_data() == elem:
                     found = True
                 else:
                 	current = current.get_next()                 	
           return found  

     def remove(self, elem):
            current = self.head
            previous = None
            found = False
            while(not found):
                if current.get_data() == elem:
                     found = True
                else:
                     previous = current
                     current = current.get_next()

            if previous == None:
            	self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            return found                                 



