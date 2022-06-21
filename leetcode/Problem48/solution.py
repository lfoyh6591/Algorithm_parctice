class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix[0])
        
        for i in range(l//2):
            for j in range(l-2*i-1):
                temp = matrix[i][j+i]
                matrix[i][j+i] = matrix[l-1-j-i][i]
                matrix[l-1-j-i][i] = matrix[l-1-i][l-1-j-i]
                matrix[l-1-i][l-1-j-i] = matrix[j+i][l-1-i]
                matrix[j+i][l-1-i] = temp