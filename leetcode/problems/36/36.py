class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for i in range(0, len(board)):
            seen = {}
            for j in range(0, len(board)):
                if board[i][j] in seen and board[i][j] != ".":
                    return False
                seen[board[i][j]] = 1
        
        # check columns
        for i in range(0, len(board)):
            seen = {}
            for j in range(0, len(board)):
                if board[j][i] in seen and board[j][i] != ".":
                    return False
                seen[board[j][i]] = 1
        
        # check boxes
        
        # one box
        for y in range(0, 7, 3):
            for x in range(0, 7, 3):
                seen = {}
                for i in range(0+y, 3+y):
                    for j in range(0+x, 3+x):
                        if board[i][j] in seen and board[i][j] != ".":
                            return False
                        seen[board[i][j]] = 1
        return True
            
        