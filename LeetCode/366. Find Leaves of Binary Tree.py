class Node:
    def __init__(self, key):
        self.left=None
        self.right=None
        self.val=key
        
def printInorder(root):
    if root:
        printInorder(root.left)
        
        print(root.val),
        
        printInorder(root.right)

def printPostoder(root):
    if root:
        printPostoder(root.left)
        printPostoder(root.right)
        print(root.val),
        
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)

#drvie code
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)
# root.left.right=Node(5)

# printPreorder(root)
printInorder(root)