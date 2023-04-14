class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        return self.items.pop()
    def push(self, item):
        return self.items.append(item)
    def peek(self):
        return self.items.index[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.push(3)
    print(s)