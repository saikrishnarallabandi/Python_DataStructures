from datastructures.stack import Stack

def decimal_to_binary(number):
        remainder_stack = Stack()

        while (number > 0):
        	rem = number % 2
        	number = number // 2
        	remainder_stack.push(rem)

        print ' '.join(str(remainder_stack.pop()))

decimal_to_binary(10)        	