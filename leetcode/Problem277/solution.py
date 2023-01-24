# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidates = [i for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    candidates.remove(i)
                    break
                
        for candidate in candidates:
            state = 1
            for i in range(n):
                if not knows(i, candidate):
                    state = 0
                    break
            if state:
                return candidate

        return -1