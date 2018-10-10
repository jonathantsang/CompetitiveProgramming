class Solution:
    destinations = dict()
    blacklist = dict()
    def checkMins(self, dp, regular, num):
        count = 1
        minVal = 9999999999
        ## print(num, "checkMins")
        ## print(regular)
        while count < 7 and count <= num:
            ## print(count, num)
            ## NOT ONLY -1
            ## print(num-count, regular[num-count] in self.destinations, num)
            if regular[num-count] == -1 or regular[num-count] in self.destinations:
                ## print(dp[num-count]+1, " in")
                minVal = min(minVal, dp[num-count]+1)
            count+=1
        return minVal
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self.destinations = dict()
        self.blacklist = dict()
        ## 1D denote board
        N = len(board)
        dp = [9999999999 for i in range(N * N)]
        i = len(board)-1
        j = 0
        regular = []
        
        ## Index
        num = 0
        dir = 'right' ## also left after
        ## print(dp)
        while i >= 0:
            ## Normal space
            regular.append(board[i][j])
            ## print(regular)
            ## If it can land there and NOT be trapped
            ## print(num, board[i][j])
            if board[i][j] == num:
                self.blacklist[num] = 1
            
            if board[i][j] != -1 and board[i][j] not in self.blacklist:
                self.destinations[board[i][j]] = 1
            
            ## Traverse board
            if dir == 'right':
                if j+1 == len(board):
                    i -= 1
                    dir = 'left'
                    j = len(board) -1
                else:
                    j += 1
            elif dir == 'left':
                if j-1 < 0:
                    i -= 1
                    dir = 'right'
                    j = 0
                else:
                    j -= 1
            num+=1
        ## print(self.destinations)
        print(regular)
        
        for num in range(0, N*N):
            ## print(dp)
            
            if regular[num] == -1:
                ## Previous six spots
                if(num == 0):
                    dp[0] = 0
                else:
                    dp[num] = min(dp[num], self.checkMins(dp, regular, num))
            else:
                portal = regular[num]
                if num >= 6:
                    dp[portal-1] = min(dp[portal-1], min(dp[num-1], dp[num-2], dp[num-3], dp[num-4], dp[num-5], dp[num-6])+1)
                    ## print(portal, dp)
                    ## dp[num] = min(dp[num], min(dp[num-1], dp[num-2], dp[num-3], dp[num-4], dp[num-5], dp[num-6])+1)
                    dp[num] = min(dp[num], self.checkMins(dp, regular, num))
                elif num >= 5:
                    dp[portal-1] = min(dp[portal-1], min(dp[num-1], dp[num-2], dp[num-3], dp[num-4], dp[num-5])+1)
                    ## print(portal, dp)
                    dp[num] = min(dp[num], self.checkMins(dp, regular, num))
                elif num >= 4:
                    dp[portal-1] = min(dp[portal-1], min(dp[num-1], dp[num-2], dp[num-3], dp[num-4])+1)
                    ## print(portal, dp)
                    dp[num] = min(dp[num], self.checkMins(dp, regular, num))
                elif num >= 3:
                    dp[portal-1] = min(dp[portal-1], min(dp[num-1], dp[num-2], dp[num-3])+1)
                    ## print(portal, dp)
                    dp[num] = min(dp[num], self.checkMins(dp, regular, num))
                elif num >= 2:
                    dp[portal-1] = min(dp[portal-1], min(dp[num-1], dp[num-2])+1)
                    ## print(portal, dp)
                    dp[num] = min(dp[num], self.checkMins(dp, regular, num))
                elif num >= 1:
                    dp[portal-1] = min(dp[portal-1], dp[num-1]+1)
                    ## print(portal, dp)
                    dp[num] = min(dp[num], self.checkMins(dp, regular, num))
                elif num == 0:
                    dp[num] = 0
                    ## Shouldn't have anything
                print(portal, dp)
                        
        print(dp)
        steps = dp[N*N-1]
        if steps == 9999999999:
            return -1
        return dp[N*N-1]