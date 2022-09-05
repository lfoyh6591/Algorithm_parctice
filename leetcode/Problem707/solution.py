class Node:
    
    def __init__(self, val, prev_node, next_node):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.root = Node(0, None, None)        
        self.len = 0
        
    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        
        temp = self.root
        for i in range(index+1):
            temp = temp.next
            
        return temp.val
        
    def addAtHead(self, val: int) -> None:
        temp = self.root.next
        
        if temp == None:
            new_node = Node(val, self.root, self.root)
            self.root.next = new_node
            self.root.prev = new_node
        
        else:
            new_node = Node(val, self.root, temp)
            self.root.next = new_node
            temp.prev = new_node
            
        self.len += 1
        
    def addAtTail(self, val: int) -> None:
        temp = self.root.prev
        
        if temp == None:
            new_node = Node(val, self.root, self.root)
            self.root.next = new_node
        else:
            new_node = Node(val, temp, self.root)
            temp.next = new_node
            
        self.root.prev = new_node
        self.len += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.len:
            self.addAtTail(val)
            return
        
        temp = self.root
        
        for i in range(index+1):
            temp = temp.next
            
        new_node = Node(val, temp.prev, temp)
        temp.prev.next = new_node
        temp.prev = new_node
        self.len += 1    

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return
        
        temp = self.root
        
        for i in range(index+1):
            temp = temp.next
            
        temp2 = temp.prev
        temp.prev.next = temp.next
        temp.next.prev = temp2
        self.len -= 1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)