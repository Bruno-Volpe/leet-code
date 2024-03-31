class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l ,r = 0, len(matrix)
        
        while l < r:
            for i in range(r-1):
                top, botton = l, r
                
                
                top_left = matrix[top][l + i]
                
                matrix[top][l + i] = matrix[botton - i][l]
                matrix[botton - i][l] = matrix[botton][r - i]
                matrix[botton][r - i] = matrix[top + i][r]
                matrix[top + i][r] = top_left
                
            l += 1
            r -= 1