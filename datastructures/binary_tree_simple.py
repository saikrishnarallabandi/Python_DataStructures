#
from queue import Queue

class BinaryTree:

	 def __init__(self, data):
	 	self.data = data
	 	self.left_child = None
	 	self.right_child = None

	 def __str__(self):
               return str(self.data)


	 def insert_left(self, value):
	    if self.left_child == None:
	        self.left_child = value
	    else:
	        t = BinaryTree(value)
	        t.left_child = self.left_child
	        self.left_child = t

	 def insert_right(self, value):
	    if self.right_child == None:
	        self.right_child = value
	    else:
	        t = BinaryTree(value)
	        t.right_child = self.right_child
	        self.right_child = t 

	 def get_left_child(self):
	    return self.left_child

	 def get_right_child(self):
	    return self.right_child   

	 def set_root_value(self, value):
	    self.data = value

	 def get_root_value(self):
	     return self.data   

'''

	 def print_tree_dfs(self, root):
            tree = root
            try:
              assert isinstance(tree, BinaryTree)
              print tree.get_root_value()
              if tree.get_left_child():
              	print "Left child is  " 
              	#print tree.get_left_child()
              	try:
                 self.print_tree_dfs(tree.get_left_child())
                except AttributeError:
                  pass
              if tree.get_right_child():
              	print "Right child is " 
              	#print tree.get_right_child()
                try:    
                 self.print_tree_dfs(tree.get_right_child())    
                except AttributeError:
                	pass
            except AssertionError:
                print tree    	

	 def print_tree_bfs(self, root_list=None):
 	  if root_list is None:
	 	  	   root_list = self.data
          for root in root_list:
            print str(root) 
            next_level = []
            if root.get_left_child():
            	next_level.append(root.get_left_child())
            if root.get_right_child():
                next_level.append(root.get_right_child())
            print self.print_tree_dfs(next_level)


         def  print_tree(self):
             queue = Queue()
             queue.enqueue(self.data)
	
             this_level = 
             print this_level

             while this_level:

             	left = self.get_left_child()
             	right = self.get_right_child()
             	print str(left) + " " + str(right)

         def print_tree(self):
           #assert isinstance(objj, BinaryTree)
           
     	   print self.data + '\n'
           this_level = self.data
           while this_level is not None:
           	   if self.data.get_left_child():
           	   	   	   r_left = self.data.get_left_child()
           	   	   	   r_left.print_tree()
           	   else:
           	      left = None	   	   
           	   if self.data.get_right_child():
           	   	        r_right = self.data.get_right_child()
           	   	        r_right.print_tree()
           	   else:
           	       right = None

           	   if left == None and right == None:
           	       this_level = None    	        
'''           	       
     



#r = BinaryTree('a')
#.insert_right('b')
#r.insert_left('c')
#r.insert_right('d')
#r.insert_left('e')

#print 'This'
#print r.get_left_child().get_root_value()

r = BinaryTree('10')
r.insert_right('11')

t = BinaryTree('9')
t.insert_right(r)
t.insert_left('7')

u = BinaryTree('6')
u.insert_right(t)




#print r.get_root_value()
#print r.get_right_child()
#print r.get_left_child()

def print_tree_dfs(root, v=None):
            tree = root
            try:
              assert isinstance(tree, BinaryTree)
              print str(tree.get_root_value()) + '_' + v
              if tree.get_left_child():
              	print "Left child is  " 
              	#print tree.get_left_child()
              	try:
                 print_tree_dfs(tree.get_left_child(), l)
                except AttributeError:
                  pass
              if tree.get_right_child():
              	print "Right child is " 
              	#print tree.get_right_child()
                try:    
                 print_tree_dfs(tree.get_right_child())    
                except AttributeError:
                	pass
            except AssertionError:
                print tree    	


#r.print_tree_dfs(u)
#print_tree_dfs(r)
#print '\n'
#r.print_tree_bfs()
#print_tree(r.get_right_child)

