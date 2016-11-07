from datastructures.dequeue import Dequeue

def palindrome_checker(p):

    p_encoder = Dequeue()

    for j in p:
    	print j
        p_encoder.add_rear(j.lower())

    while (p_encoder.size() > 0):
    	 a = p_encoder.remove_front()
    	 z = p_encoder.remove_rear()
    	 print a
    	 print z
         if a == z:
                    pass
         else:
                    print "Not palindrome"
                    return
    print "Palindrome"                 

palindrome_checker("Malayalam")