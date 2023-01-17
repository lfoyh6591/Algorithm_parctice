class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    l.append((i, j))

        while l:
            m, n = l.pop()
            for i in range(len(matrix[0])):
                matrix[m][i] = 0
            for i in range(len(matrix)):
                matrix[i][n] = 0