class Stack:
    def __init__(self):
        self.top=-1
        self.length=0
        self.items=[]

    def isEmpty(self):
        if self.top==-1:
            return True

    def push(self,key):
        self.items.append(key)
        self.top=self.top+1
        self.length=self.length+1

    def Spop(self):
        if self.top==-1:
            return "Stack already empty"
        else:
            self.top=self.top-1
            self.length=self.length-1
            return self.items.pop()

s=Stack()
print(s.top,s.length,s.items)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.items)
print(s.Spop())
print(s.top,s.length,s.items)



