class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1 for i in range(k)]
        self.start = 0
        self.end = 0
        self.len = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.q[self.end] = value
        self.end = (self.end+1) % self.len
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.q[self.start] = -1
        self.start = (self.start+1) % self.len
        return True        

    def Front(self) -> int:
        return self.q[self.start]

    def Rear(self) -> int:
        return self.q[self.end-1]

    def isEmpty(self) -> bool:
        return (self.end == self.start) and (self.q[self.start] == -1)

    def isFull(self) -> bool:
        return (self.end == self.start) and (self.q[self.start] != -1)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()