class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # BACKTRACKING
        # Time: O(N * 4^L) where N is the number of cells in the board and L is the length of the word
        # Space: O(L) where L is the length of the word
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i] or (r, c) in path:
                return False
            path.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False