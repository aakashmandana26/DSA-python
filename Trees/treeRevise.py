class BST:
    def __init__(self,key):
        self.key=key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if(self.key is None):
            self.key = data
        
        else:

            if(self.key > data):
                if(self.lchild is None):
                    self.lchild=BST(data)
                    return
                else:
                    self.lchild.insert(data)

            else:
                if(self.rchild is None):
                    self.rchild = BST(data)
                    return
                else:
                    self.rchild.insert(data)

    def search(self, data):
        if(self.key is None):
            print("Node not present!")
            return

        elif(self.key > data):
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Given node not present")
                return

        elif(self.key < data):
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Given node not present")
                return
            
        else:
            print("NODE FOUND!")
            return

    def preorder(self):
        if (self.key is None):
            return

        else:
            print(self.key, end=" ")
            if (self.lchild):
                self.lchild.preorder()
            if(self.rchild):
                self.rchild.preorder()
            return

    def inorder(self):
        if(self.key is None):
            return
        else:
            if(self.lchild):
                self.lchild.inorder()
            print(self.key, end=" ")
            if(self.rchild):
                self.rchild.inorder()

    def postorder(self):
        if(self.key is None):
            return
        else:
            if(self.lchild):
                self.lchild.postorder()
            if(self.rchild):
                self.rchild.postorder()
            print(self.key, end=" ")

    def delete(self, data):
        if(self.key is None):
            print("Tree is already empty!")
            return

        elif(self.key > data):
            if(self.lchild):
                self.lchild = self.lchild.delete(data)
            else:
                print("Node not found")

        elif(self.key < data):
            if(self.rchild):
                self.rchild = self.rchild.delete(data)
            else:
                print("Node not found")
            
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
                while(temp.rchild is not None):
                    temp = temp.rchild

                self.key=temp.key
                self.lchild = self.lchild.delete(temp.key)
            
        return self
                


        






root = BST(50)
root.insert(25)
root.insert(15)
root.insert(20)
root.insert(100)
root.insert(30)
print(root.lchild.key)
print(root.lchild.lchild.key)

root2 = BST(None)
root2.insert(2)
print(root2.key)
root.search(15)
print()
root.preorder()
print()
root.inorder()
print()
root.postorder()
print()

root.delete(50)
root.preorder()

            
