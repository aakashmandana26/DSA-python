class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
        else:

            n = self.head
            while(n is not None):
                print(n.data ,end=" -> ")
                n = n.ref

    
    def addBeginningNode(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.ref = self.head
            self.head = newNode
        

    def addEndNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while(n.ref is not None):
                n=n.ref
            n.ref = newNode


    def addBefore(self,xnode,newdata):
        newNode = Node(newdata)
        if(self.head is None):
            print("Linked List is empty")
        elif self.head.data==xnode:
            newNode.ref = self.head
            self.head = newNode
        else:
            n = self.head
            while(n.ref is not None):
                if(n.ref.data == xnode):
                    newNode.ref = n.ref
                    n.ref = newNode
                    break
                n = n.ref
            if(n.ref is None):
                print("Given node doesnt exist!")

    
    def addAfter(self, xnode, newdata):
        newNode = Node(newdata)

        if(self.head is None):
            print("Linked list is empty")
        elif(self.head.data==xnode):
            self.head.ref=newNode
        else:
            n = self.head
            while(n.ref is not None):
                if(n.ref.data == xnode):
                    n=n.ref
                    newNode.ref = n.ref
                    n.ref = newNode
                    break
                n=n.ref
            if(n.ref is None):
                print("Given node doesnt exist")


    def delNode(self, nodeData):
        if(self.head is None):
            print("Linked list was empty")

        elif(self.head.data==nodeData):
            self.head = self.head.ref
            
            print("Node deleted")

        else:
            nodeDeleted = False
            print("true")
            n=self.head
            while(n.ref is not None):
                if(n.ref.data==nodeData):
                    n.ref=n.ref.ref
                    
                    print("Node deleted")
                    nodeDeleted = True
                    break
                n=n.ref
            
            if(n.ref is None and nodeDeleted==False):
                print("Given node doesnt exist")

ll1 = LinkedList()
ll1.addBeginningNode(5)
ll1.addAfter(5,10)
ll1.addBefore(5,1)
ll1.addBefore(10,6)
ll1.addEndNode(100)
ll1.addAfter(100,1000)
ll1.delNode(6)
ll1.printLL()