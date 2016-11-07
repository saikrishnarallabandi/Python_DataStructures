#

class min_heap:

     def __init__(self):
          self.heap_list = [0]
          self.size = 0

     def swap(self, a, b):
     	  print ' I got ' + str(a) + ' and ' + str(b)
          print 'Swapping ' + str(a) + ' and ' + str(b)
          return b, a     

     def insert_helper(self, n):
          while( (n // 2) > 0  ):
             if self.heap_list[n] < self.heap_list[(n // 2)]:
                        #self.heap_list[n], self.heap_list[(n//2)] = self.swap(self.heap_list[n], self.heap_list[(n//2)])
                   tmp = self.heap_list[n // 2]
                   self.heap_list[ n//2] = self.heap_list[n]
                   self.heap_list[n] = tmp

             n = n// 2
          print ' The heap now looks like this:'   
          self.print_heap()   

     def insert(self, data):
     	  print "Inserting " + str(data)
          self.heap_list.append(data)
          self.size = self.size + 1
          self.insert_helper(self.size)

     def print_heap(self):     
          print ' '.join(str(i) for i in self.heap_list)
   

a = min_heap()
a.insert('3')
a.insert('2')
a.insert('7')
a.insert('1') 
a.print_heap()         
a.insert('2')
a.insert('7')
a.insert('1')
a.print_heap()
