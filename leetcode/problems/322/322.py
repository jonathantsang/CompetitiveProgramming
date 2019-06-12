class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [9999 for i in range(0, amount+1)]
        if amount == 0:
            return 0
        coins.sort()
        for i in range(0, amount+1):
            for j in range(0, len(coins)):
                # Each coin valid
                if coins[j] > i:
                    break
                elif coins[j] == i:
                    dp[i] = 1
                    break
                else:
                    dp[i] = min(dp[i - coins[j]] + 1, dp[i])
        if dp[amount] == 9999:
            return -1
        else:
            return dp[amount]