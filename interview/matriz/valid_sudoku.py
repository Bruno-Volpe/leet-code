class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            digits = [0] * 9
            
            # Check for repeated digits in the row
            for element in board[row]:
                if element != '.':
                    if element not in digits:
                        digits[int(element) - 1] = element
                    else:
                        return False
                
        for column in range(9):
            digits = [0] * 9
            
            # Check for repeated digits in the column
            for row in range(9):
                element = board[row][column]
                if element != '.':
                    if element not in digits:
                        digits[int(element) - 1] = element
                    else:
                        return False
                
        #Check the grids
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                digits = [0] * 9
                
                # Check for repeated digits in the grid
                for r in range(row, row+3):
                    for c in range(column, column+3):
                        element = board[r][c]
                        if element != '.':
                            if element not in digits:
                                digits[int(element) - 1] = element
                            else:
                                return False
        return True
