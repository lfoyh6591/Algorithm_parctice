class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        check = [[False]*n for i in range(m)]
        check[0][0] = True
        q = [(matrix[0][0], 0, 0)]
        while q:
            val, x, y = q.pop(0)
            if val == target:
                return True
            
            if x+1 < m:
                if not check[x+1][y]:
                    check[x+1][y] = True
                    q.append((matrix[x+1][y], x+1, y))
            
            if y+1 < n:
                if not check[x][y+1]:
                    check[x][y+1] = True
                    q.append((matrix[x][y+1], x, y+1))

        return False