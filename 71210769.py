class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True

    def getData(self):
        return self.data
    
    def getleft(self):
        return self.left

    def getright(self):
        return self.right
    
    def getparent(self):
        return self.parent

    def isRoot(self):
        return self.parent is None

    def isExternal(self):
        return self.left is None and self.right is None

class BinaryTree:
    def __init__(self):
        self.root = Node(0,None)
        self._size = 0
    
    def add(self, data):
        if self.root.left is None and data%2 != 0:
            self.root.left = Node(data,self.root)
        elif self.root.right is None and data%2 == 0:
            self.root.right = Node(data,self.root)
        else:
            if data%2 != 0:
                self.root.left.insert(data)
            else:
                self.root.right.insert(data)
    
    def size(self):
        return self._size

    def empty(self):
        return self._size == 0
    
    def nodes(self):
        self.inorder(self.root)
    
    def nodes1(self):
        self.preorder(self.root)

    #inorder traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.getleft())
            print(node.getData(), end = ' ')
            self.inorder(node.getright())
    
    def preorder(self, node):
        if node is not None:
            print(node.getData(), end = ' ')
            self.preorder(node.getleft())
            self.preorder(node.getright())

    def sumGenap(self,node,genap=[]):
        if node is not None:
            self.sumGenap(node.left)
            if node.data % 2 == 0:
                genap.append(node.data)
            self.sumGenap(node.right)
        return sum(genap)

    def hasilGenap(self):
        return f"Penjumlahan data genap = {self.sumGenap(self.root)}"

tree = BinaryTree()
tree.add(5)
tree.add(4)
tree.add(3)
tree.add(9)
tree.add(8)
tree.add(6)
tree.add(7)
tree.add(11)
tree.add(10)
print("dalam inorder =",end = ' '),tree.nodes()
print()
print("dalam preorder =",end= ' '),tree.nodes1()