class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        dp = [9999999 for i in range(0, 365+30)]
        dp[0] = 0
        m = max(days)
        for i in range(1, m+1):
            dp[i] = min(dp[i], dp[i-1] + costs[0]) # buy 1 day pass?
            dp[i+6] = min(dp[i+6], dp[i-1] + costs[1]) # buy 7 day pass
            dp[i+29] = min(dp[i+29], dp[i-1] + costs[2])
        cost = 0
        for d in days:
            cost += dp[d]
        return cost