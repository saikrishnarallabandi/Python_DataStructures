#!/usr/bin/python

class Node:

	 def __init__(self,data):
	     self.data = data
	     self.next = None

	 def get_data(self):
	     return self.data

	 def set_data(self, new_data):
             self.data = new_data

         def get_next(self):
             return self.next

         def set_next(self, value):
             self.next = value

class Linkedlist:
  
     def __init__(self):
          self.head = None

     def is_empty(self):
          return self.head == None

     def add(self, new_data):
       	 node = Node(new_data)
       	 node.set_next(self.head)
       	 self.head = node 

     def size(self):
     	 count = 0
     	 current = self.head

     	 while (current is not None):
     	 	count = count + 1
     	 	current = current.get_next()
     	 return count	

     def search(self, data):
         found = false
         current = self.head
         while( not found and current is not None):
              if (current.get_data() == data):
              	  found = true
              	  #return current
              else:
                  current = current.get_next()
         return found

     def delete(self, data):
         found = false
         previous = None
         current = self.head

         while(not found and current is not None):
             if (current.get_data() == data):
                  found = true
             else:
                 current = current.get_next()
                 previous = current                    
         if (found is false):
         	print "Not found"
         elif (previous == None):
            self.head = current.get_next()	
         else:
         	previous.set_next(current.get_next())

     def print_list(self):
         l = []
         current = self.head

         while( current is not None):
             l.append(current.get_data())
             current = current.get_next()
         return '->'.join(l[i] for i in range(len(l)))

a = Linkedlist()
a.add('2')
a.add('3')
a.add('4')
a.add('7')
print a.is_empty()         	 
print a.print_list()
    