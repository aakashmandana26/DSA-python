class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        elif(self.key>data):
            
            if self.lchild:
                self.lchild.insert(data)
            else:
                
                self.lchild = BST(data)
                return

        else:
            
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                return

    def search(self, data):
        if self.key is None:
            print("Given data not present")
            return

        elif(data == self.key):
            print("Node present")
            return

        elif(data < self.key):
            if(self.lchild):
                self.lchild.search(data)
            else:
                print("Given node not present")
                return
        else:
            if(self.rchild):
                self.rchild.search(data)
            else:
                print("Given node not present")
                return

    def preorder(self):
        print(self.key, end=" ")

        if(self.lchild):
            self.lchild.preorder()
        if(self.rchild):
            self.rchild.preorder()
        
    def inorder(self):
        if(self.key is None):
            return None
        else:
            if(self.lchild):
                self.lchild.inorder()
            print(self.key, end=" ")
            if(self.rchild):
                self.rchild.inorder()

    def postorder(self):
        if(self.key is None):
            return None
        else:
            if(self.lchild):
                self.lchild.postorder()
            if(self.rchild):
                self.rchild.postorder()
            print(self.key, end=" ")

    def delete(self, data):
        if(self.key is None):
            print("Tree is empty!")
            return

        elif(data < self.key):
            if(self.lchild):
                self.lchild = self.lchild.delete(data)
            else:
                print("Node not found in the tree")
                return
        elif(data > self.key):
            if(self.rchild):
                self.rchild = self.rchild.delete(data)
            else:
                print("Node not found in the tree")
                return
        
        else:
            if(self.lchild is None):
                temp = self.rchild
                self = None
                return temp
            elif(self.rchild is None):
                temp = self.lchild
                self = None
                return temp
            else:
                temp = self.lchild
                while(temp.rchild):
                    temp = temp.rchild
                self.key = temp.key
                self.lchild = self.lchild.delete(temp.key)
        return self

    
    def deleteRoot(self):
        if(self.key is None):
            print("Tree is already empty!")

        elif(self.lchild is None):
            # print(self.rchild, "is None")
            self = self.rchild
            return self
        elif(self.rchild is None):
            return self.lchild

        else:
            temp = self.lchild
            if(temp.rchild is None):
                temp.rchild = self.rchild
                return temp
            while(temp.rchild.rchild):
                temp = temp.rchild
            self.key = temp.rchild.key
            temp.rchild = None
            return self

        
    def count_nodes(self):
        if(self is None):
            return 0
        if(self.lchild is None):
            return 0
        if(self.rchild is None):
            return 0
        return 1+self.lchild.count_nodes()+self.rchild.count_nodes()
                
root = BST(10)
root.lchild = BST(5)
root.rchild = BST(15)
childs = [20,2,4,6,7,9,10]
for i in childs:
    root.insert(i)

# print(root.rchild.lchild.key)

# root2 = BST(None)

# root2.preorder()
# print()
# root2.insert(50)
# root2.preorder()
# root2.deleteRoot()
# root2.preorder()
# print(root.count_nodes())

root.preorder()
print()
root.deleteRoot()
root.preorder()
print("")
print(root.count_nodes())





