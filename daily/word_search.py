class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # BACKTRACKING
        # Time: O(N * 4^L) where N is the number of cells in the board and L is the length of the word
        # Space: O(L) where L is the length of the word
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[i]:
                return False
            board[r][c] = '#'
            res = backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1)
            board[r][c] = word[i]
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        return False