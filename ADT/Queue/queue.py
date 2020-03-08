class Linearqueue:
    def __init__(self):
        self.front=0
        self.rear=-1
        self.elements=[]

    def insertInQueue(self,key):
        self.elements.append(key)
        self.rear=self.rear+1

    def removeFromQueue(self):
        if self.rear == 0:
            print("Queue Already empty")
        else:
            self.elements.pop(self.front)
            self.rear=self.rear-1
    def getFrontElement(self):
        return self.elements[self.front]

    def getRearElement(self):
        return self.elements[self.rear]

q=Linearqueue()
print(q.rear,q.front)
q.insertInQueue(10)
q.insertInQueue(20)
q.insertInQueue(30)
q.insertInQueue(40)
print(q.elements)

print(q.getFrontElement())







