class Vector2D:

    def __init__(self, vec: list[list[int]]):
        self.vec = vec
        self.q = []
        for v in self.vec:
            for i in range(len(v)):
                self.q.append(v[i])
        self.cur = 0

    def next(self) -> int:
        self.cur += 1
        return self.q[self.cur-1]

    def hasNext(self) -> bool:
        if self.cur < len(self.q):
            return True
        else:
            return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()