def same(mat, target):
    l = len(mat[0])
    for i in range(l):
        for j in range(l):
            if mat[i][j] != target[i][j]:
                return False
    return True

def clockwise(mat, target):
    l = len(mat[0])
    for i in range(l):
        for j in range(l):
            if mat[i][j] != target[j][-1-i]:
                return False
    
    return True

def sym(mat, target):
    l = len(mat[0])
    for i in range(l):
        for j in range(l):
            if mat[i][j] != target[-1-i][-1-j]:
                return False
            
    return True

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if clockwise(mat, target) or clockwise(target, mat) or sym(mat, target) or same(mat, target):
            return True