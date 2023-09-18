class BST():
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, val):
        if self.key is None:
            self.key = val
            return
        
        else:
            if(self.key > val):
                if(self.lchild):
                    self.lchild.insert(val)
                else:
                    self.lchild = BST(val)
                    return
            
            else:
                if(self.rchild):
                    self.rchild.insert(val)
                else:
                    self.rchild = BST(val)
                    return

        
    def preorder(self):
        print(self.key, end=" ")
        if(self.lchild):
            self.lchild.preorder()
        if(self.rchild):
            self.rchild.preorder()

    def inorder(self):
        if(self.lchild):
            self.lchild.inorder()
        print(self.key, end=" ")
        if(self.rchild):
            self.rchild.inorder()

    def postorder(self):
        if(self.lchild):
            self.lchild.postorder()
        if(self.rchild):
            self.rchild.postorder()
        print(self.key, end=" ")

    
    def search(self, val):
        if(self.key is None):
            print("Tree is empty")
            return
        else:
            if(self.key == val):
                print("Key found")
                return
            elif(self.key > val):
                if(self.lchild):
                    self.lchild.search(val)
                else:
                    print("Key not found")
                    return
            else:
                if(self.rchild):
                    self.rchild.search(val)
                else:
                    print("Key not found")
                    return
    
    def countNodes(self):
        if(self.key is None):
            return 0
        if(self.lchild is None):
            return 0
        if(self.rchild is None):
            return 0
        
        return 1+self.lchild.countNodes()+self.rchild.countNodes()
            



t1 = BST(None)
t1.insert(50)
t1.insert(25)
t1.insert(60)
t1.insert(100)
t1.insert(10)
t1.insert(30)
t1.insert(55)

t1.preorder()
print("")
t1.inorder()
print("")
t1.postorder()
print("")

t1.search(40)
t1.search(55)

print(t1.countNodes())
    #         50
    #     25      60
    # 10     30 55    100

arr=[9,4,20,1,6,15,170]
t2 = BST(None)
for i in arr:
    t2.insert(i)
t2.preorder()
