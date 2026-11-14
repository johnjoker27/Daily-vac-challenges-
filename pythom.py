class ArrayStack:

    def __init__(self, capacity = 10):
        self.items = [None] * capacity 
        self.capacity = capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1
    

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self , value):
        if self.is_full():
            raise OverflowError("push tp a full stack")
        self.top += 1
        self.items[self.top] = value


    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        value = self.items[self.top]
        self.items[self.top] = None 
        self.top -= 1
        return value

    def peak(self):
        return self.top + 1

    def size(self):
        return self.capacity


ars = ArrayStack(5)
ars.push("A")
ars.push("b")
ars.push("c")
print(ars.is_full())
ars.pop()
ars.push("C")
ars.push("G")
ars.push("f")
ars.push("w")
print(ars.size())


#capacity = 5, push abc check is full,pop, push cgf size()
class Linkedstack:

    def __init__(self,capacity = 5):
            self.items = [None] * capacity
            self.capacity = capacity
            self.top = -1
            

    def is_empty(self):
            return self.top == -1

        