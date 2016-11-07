from datastructures.stack import Stack

def decimal_to_binary(number):
        remainder_stack = Stack()

        while (number > 0):
        	rem = number % 2
        	#print rem
        	number = number // 2
        	#print number
        	remainder_stack.push(rem)

        s = ''
        for k in range(remainder_stack.size()):
             s += str(remainder_stack.pop())
        print s
decimal_to_binary(10)        	