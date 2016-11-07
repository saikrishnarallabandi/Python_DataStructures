
class Tree:

    def __init__(self, root, left_child=None, right_child=None):
	  self.root = root
	  self.left_child = left_child
	  self.right_child = right_child

	  def get_root_value(self):
	      return self.root

	  def get_left_child(self):
	      return self.get_left_child

	  def get_right_child(self):
	      return self.get_right_child        

	  def set_root_value(self, new_root):
	      self.root = new_root

	  def __str__(self):
	      return str(self.root)   

	  def insert_left_child(self, root, left_child):
              print self.left_child
	      if self.left_child == None:
	            self.left_child = left_child
              else:
          	  t = Tree(root)
          	  t.left_child = left_child
          	  self.left_child = t
          	  print "Inserted " + str(left_child) + ' to the left of ' + root
    
	  def insert_right_child(self, root, right_child):
	      if self.right_child == None:
	            self.right_child = right_child
              else:
          	  t = Tree(root)
          	  t.right_child = right_child
          	  self.right_child = t  
              print "Inserted " + str(right_child) + ' to the right of ' + root


          def print_tree(self,level=0):
              print level * ' ' + self.root
              #print self.left_child
              try:
                self.left_child.print_tree(level+1)
              except AttributeError:
                print (level+1) * ' ' + str(self.left_child)
              try:  
                self.right_child.print_tree(level+1)               
              except AttributeError:
              	 print (level+1) * ' ' + str(self.right_child)
       
          def max_depth(self, n):
             printn
             if n.get_left_child() == None and n.get_right_child == None:
             	 return 1
             else:
                 return 1 + min(min_depth(x) for x in [n.get_left_child(), n.get_right_child()])	 

          def min_depth(self, n):
             if n.get_left_child() == None and n.get_right_child == None:
             	 return 1
             else:
                 return 1 + max(max_depth(x) for x in [n.get_left_child(), n.get_right_child()])	 

          def is_balanced(self, n):
              print n
              print self.max_depth(n)
              return self.max_depth(n) - self.min_depth(n) < 2


         # Traversals
         def traverse(self, func, level=0):
             if self.left:
                  self.left.traverse(func, level+1)
             func(self, level)
             if self.right:
                  self.right.traverse(func, level+1)


t = Tree('1')
t.insert_left_child('1', '1_l')
t.insert_right_child('1', '1_r')
t.insert_left_child('1_l', '1_l_l')
t.insert_right_child('1_r', '1_r_r')

print t.print_tree()
print t.is_balanced('1')
