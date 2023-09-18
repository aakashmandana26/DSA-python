
from tkinter import N


class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
    
class DoubleLL:
    def __init__(self):
        self.head = None

    def printLL(self):
        n=self.head
        if(n is None):
            print("Linked list is empty")
            
        while(n is not None):
            print(n.data,"-->",end="")
            n=n.nref
        print()

    def printRevLL(self):
        n=self.head
        while(n.nref is not None):
            n=n.nref
        while(n is not None):
            print(n.data,"-->",end="")
            n=n.pref
        print()

    def addEndNode(self,data):
        newNode = Node(data)
        n=self.head
        if(n is None):
            self.head=newNode
        else:
            while(n.nref is not None):
                n=n.nref
            n.nref=newNode
            newNode.pref=n

    def addFirstNode(self,data):
        newNode = Node(data)
        n=self.head
        if(n is None):
            self.head=newNode
        else: 
            newNode.nref=n
            n.pref = newNode
            self.head = newNode

    def deleteEndNode(self):
        n=self.head
        if(n is None):
            print("Linked list is already empty")
        elif(n.nref is None):
            self.head=None
 
        else:
            while(n.nref is not None):

                n=n.nref  
            n=n.pref
            n.nref=None
        
    def deleteFirstNode(self):
        n=self.head
        if(n is None):
            print("Linked list is already empty")
        else:
            self.head=n.nref
            if(n is not None):
                n.pref=None

    def deleteByValue(self,val):
        n=self.head
        if(n is None):
            print("DLL is empty, cant delete!")
            return
        elif(n.nref is None):
            if(n.data==val):
                self.head=None
                print("Node deleted")
                return
            else:
                print("Given node not present in DLL")
                return
        else:
            while(n.nref is not None and n.nref.data!=val):
                n=n.nref
            if(n.nref is None):
                print("Given node not present in DLL")
            elif(n.nref.nref is None):
                n.nref = None
            else:
                n.nref = n.nref.nref
                n=n.nref
                n.pref=n.pref.pref





    # def addByIndex(self,data, index):
    #     newNode = Node(data)
    #     n=self.head
    #     if(index==0):
    #         newNode.nref=n
    #         n.pref=newNode
    #         self.head=newNode
    #     else:
    #         i=0
    #         while(i<index-1 and n.nref is not None):
    #             n=n.nref
    #             i+=1
            
    #         n.nref=newNode
    #         newNode.pref=n
    #         newNode.nref=n.nref.nref




            



n1= Node(5)
n2= Node(10)
n1.nref=n2
n2.pref=n1
ll1 = DoubleLL()
ll1.head = n1
ll1.addEndNode(15)
ll1.addFirstNode(0)
# ll1.addByIndex(20,3)
ll1.deleteByValue(0)


ll1.printLL()

