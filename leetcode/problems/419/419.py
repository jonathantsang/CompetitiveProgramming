class Solution:
    def traverse(self, board, seen, i, j):
        if seen[i][j] == 1:
            return
        seen[i][j] = 1
        if i - 1 >= 0 and board[i-1][j] == 'X':
            self.traverse(board, seen, i-1, j)
        if i + 1 < len(board) and board[i+1][j] == 'X':
            self.traverse(board, seen, i+1, j)
        if j - 1 >= 0 and board[i][j-1] == 'X':
            self.traverse(board, seen, i, j-1)
        if j + 1 < len(board[0]) and board[i][j+1] == 'X':
            self.traverse(board, seen, i, j+1)
        
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        components = 0
        seen = [ [0 for y in range(0, len(board[0]))] for x in range(0, len(board))]
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'X' and seen[i][j] == 0:
                    components += 1
                    self.traverse(board, seen, i, j)
        return components
        
# go through the board row by row
# mark the seen as seen
# count number of components