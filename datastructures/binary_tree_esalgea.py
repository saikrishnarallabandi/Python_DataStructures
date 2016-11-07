# https://esalagea.wordpress.com/2012/09/25/cracking-the-coding-interview-4-1-balanced-tree/


class TreeNode(object):
    def __init__(self,data,children=None):
        self.data=data
        if children is None:
            self.children=[]
        else:
            self.children=children

        def addChild(self, node):
            self.children.append(child)
 
        def show(self,level=0):
            print level*"          " + self.data
            for child in self.children:
                child.show(level+1)

def isBalanced(n):
            
            return maxDepth(n) - minDepth(n) < 2
        
def minDepth(n):
            print n.children
            if n.children==[]:
                 return 1
            return  1+ min (minDepth(x) for x in n.children)
 
def maxDepth(n):
            #print n.children
            if n.children==[]:
                 return 1
            return  1+ max (maxDepth(x) for x in n.children)
    


def test():
    n1 = TreeNode("1")
    n2 = TreeNode("2")  
    n3 = TreeNode("3",[n1,n2])
    n4 = TreeNode("4")
    n5 = TreeNode("5",[n4])
    n6 = TreeNode("6",[n5])
    n7 = TreeNode("7",[n6,n3])
    #n7.show()
    assert(minDepth(n7)==3)
    assert(maxDepth(n7)==4)
    assert(isBalanced(n7))
    assert(minDepth(n6)==3)
    assert(maxDepth(n6)==3)
    assert(isBalanced(n6))
    print isBalanced((n6))

    print '\n\n'
    print maxDepth(n3)
    print n3.data
    print n3.children
    print n3
 
if __name__=='__main__':
    test()
