class BST:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

# -------- Inserting new nodes ----------- 
    def insert(self,data):
        if self.data is None:
            self.data = data
            return
        if self.data == data:
            return
        if self.data > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

# -------- Preorder Traversal ----------- 
    def preorder(self):
        print(self.data)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

# -------- Inorder Traversal ----------- 
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data)
        if self.rchild:
            self.rchild.inorder()

# -------- Postorder Traversal ----------- 
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data)
    
# -------- Searching -----------     
    def search(self,data):
        if self.data == data:
            print("Data is found!")
            return
        if data < self.data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Data is not found!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Data is not found!")

# Initializing object / BST root is none
root = BST(None)

#Adding elements to the list
list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	elements = int(input())
	list1.append(elements)

# Inserting list elements to the nodes
for i in list1:
    root.insert(i)
  
# Preorder Traversal
print("Preorder- ")
root.preorder()

# Inorder Traversal
print("Inorder- ")
root.inorder() 

# Postorder Traversal
print("Postorder- ")
root.postorder()

# Performing Search Operation
print("Searching- ")
val = int(input("Enter the item to search- "))
root.search(val)
