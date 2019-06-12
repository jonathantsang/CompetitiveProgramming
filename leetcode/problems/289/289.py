class Solution:
    def countLiveNeigh(self, board, i, j, n, m):
        count = 0 
        directions = [(1,0), (0,1), (-1,0), (0,-1), (-1,1), (1,-1), (1,1), (-1,-1)]
        for direction in directions:
            new_row = i + direction[0]
            new_col = j + direction[1]
            if (0 <= new_row < n) and (0 <= new_col < m):
                count += board[new_row][new_col]

        return count
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0]) if n > 0 else 0
        state = [[0 for x in range(0,m)] for y in range(0, n)]
        for i in range(0, n):
            for j in range(0, m):
                live = self.countLiveNeigh(board, i, j, n, m)
                if board[i][j] == 1:
                    if live < 2:
                        state[i][j] = 0
                    elif live == 2 or live == 3:
                        state[i][j] = 1
                    elif live > 3:
                        state[i][j] = 0
                else:
                    if live == 3:
                        state[i][j] = 1
                    else:
                        state[i][j] = 0
        # Then copy state over
        for i in range(0, n):
            for j in range(0, m):
                board[i][j] = state[i][j]