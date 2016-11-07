from datastructures.queue import Queue

names = ["A",  "B", "C", "D", "E"]
num = 2
def hotpotato(names,num):
     circular_queue = Queue()

     for name in names:
         circular_queue.enqueue(name)
 
     while circular_queue.size() > 1:
      for k in range(num-1):
         circular_queue.enqueue(circular_queue.dequeue())
      circular_queue.dequeue()
     print circular_queue.dequeue()

hotpotato(names,num)
