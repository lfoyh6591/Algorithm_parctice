import random

class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.len = 0
        
    def insert(self, val: int) -> bool:
        self.set = self.set | set([val])
        
        if self.len == len(self.set):
            return False
        else:
            self.len += 1
            return True

    def remove(self, val: int) -> bool:
        self.set = self.set - set([val])
        if self.len == len(self.set):
            return False
        else:
            self.len -= 1
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()