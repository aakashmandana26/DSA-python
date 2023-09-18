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
ll1.printLL()

node1 = Node(10)
ll1.head = node1

node2 = Node(20)
node1.ref = node2
# print(node1.data)
# print(node1.ref.data)
# ll1.printLL()
ll1.addBeginningNode(5)
ll1.printLL()
print("\n This is linked list 2")

ll2= LinkedList()
ll2.printLL()
ll2.addBeginningNode(100)
ll2.printLL()
print()
ll2.addEndNode(200)
ll2.addBeginningNode(50)
ll2.printLL()
print("\nthis is linked list 3")

ll3 = LinkedList()
ll3.printLL()
ll3.addEndNode(1)
ll3.addBefore(1,0)
ll3.addBefore(0,-1)
ll3.addBefore(1,5)
ll3.addBefore(6,10)
ll3.addAfter(0,2)
ll3.addAfter(1,3)
ll3.addAfter(4,8)
ll3.printLL()
print('\nThis is linked list 4')
ll4 = LinkedList()
ll4.addBeginningNode(5)
ll4.addAfter(5,10)
ll4.delNode(10)
ll4.delNode(5)
ll4.printLL()


