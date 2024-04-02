class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top, left, right, bottom = 0, 0, len(matrix[0]), len(matrix)
        
        while top < bottom and left < right:
            #Setar limites para linha e coluna em que o 0 estao
            for i in range(left, right):
                if matrix[top][i] == 0:
                    for j in range(top, bottom):
                        matrix[j][i] = 0
                    for j in range(left, right):
                        matrix[top][j] = 0
                    break
            top += 1
            