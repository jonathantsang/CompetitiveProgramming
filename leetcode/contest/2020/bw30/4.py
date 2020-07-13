class Solution:
    def winnerSquareGame(self, n: int) -> bool:

#         @lru_cache(None)
#         def topdown(n):
#             if n == 0:
#                 return True
#             if n == 1:
#                 return True

#             j = 1
#             val = j**2
#             while val <= n:
#                 val = j**2
#                 if topdown(n-val):
#                     return True

#             return False

        dp = [0 for _ in range(n+1)] # 1 first person can win, 0 second person can win
        dp[1] = 1

        for i in range(2,n+1):
            j = 1
            val = j**2
            while val <= i:
                if dp[i-val] == 0:
                    dp[i] = 1
                    break
                j+=1
                val = j**2
        return dp[n]

        #return topdown(n)
