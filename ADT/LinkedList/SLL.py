class Node:
    def __init__(self,key):
        self.next=None
        self.key=key

class SLL:
    def __init__(self):
        self.head=None
        self.NoOfNodes=0

    def addNode(self,key):
        newNode = Node(key)
        if self.head is None:
            self.head = newNode
            self.NoOfNodes= self.NoOfNodes+1
        else:
            lastNode= self.getLastNode()
            lastNode.next = newNode
            self.NoOfNodes = self.NoOfNodes + 1

    def getLastNode(self):
        currentNode= self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        return currentNode

    def insertNodeAtPosition(self,position,key):
        newNode = Node(key)
        nodeBeforePosition = self.getNodeAtPosition(position-1)
        newNode.next = nodeBeforePosition.next
        nodeBeforePosition.next = newNode

    def getNodeAtPosition(self,position):
        currentNode = self.head
        for i in range(1,position):
            currentNode = currentNode.next
        return currentNode

    def deleteNodeAtPosition(self,position):
        nodeBeforePosition = self.getNodeAtPosition(position-1)
        nodeBeforePosition.next = nodeBeforePosition.next.next

    def search(self,key):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.key ==key:
                return "Found"
            currentNode = currentNode.next
        return "Not Found"

    def display(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.key)
            currentNode = currentNode.next


myll = SLL()
myll.addNode(6)
myll.addNode(7)
myll.addNode(8)
myll.addNode(9)
myll.insertNodeAtPosition(3,10)
myll.deleteNodeAtPosition(3)
myll.display()
print(myll.search(11))







