from datastructures.binary_tree_simple import BinaryTree
from datastructures.queue import Queue

#Given a binary tree, we need to find length of the longest consecutive sequence path where path refers to sequence of node in tree along with parent child connection.

r = BinaryTree('10')
r.insert_right('11')

t = BinaryTree('9')
t.insert_right(r)
t.insert_left('7')

u = BinaryTree('6')
u.insert_right(t)

count = 0
typ = 'root'




#print r.get_root_value()
#print r.get_right_child()
#print r.get_left_child()

def print_tree_dfs(root, v='root'):
            tree = root
            global count
            global typ
            try:
              assert isinstance(tree, BinaryTree)
              print str(tree.get_root_value()) + '_' + v
              if typ == v:
            	count = count+1     	
              else:
               typ = v
               count = 0

              if tree.get_left_child():
                try:
                 print_tree_dfs(tree.get_left_child(), 'Left')
                 if typ == v:
            	    count = count+1     	
                 else:
                    typ = v
                    count = 0
                 print count                     
                except AttributeError:
                  print count
              if tree.get_right_child():
              	#print "Right child is " 
              	#print tree.get_right_child()
                try:    
                 print_tree_dfs(tree.get_right_child(), 'Right')
                 if typ == v:
            	    count = count+1     	
                 else:
                    typ = v
                    count = 0  
                 print count     
                except AttributeError:
                	print count
            except AssertionError:
                print str(tree) + '_' + v 


            if typ == v:
            	count = count+1     	
            else:
               typ = v
               count = 0
            print count   

print_tree_dfs(u)