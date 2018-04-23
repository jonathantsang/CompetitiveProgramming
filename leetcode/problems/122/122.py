class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        leng = len(prices)
        maxp = 0
        for i in range(0, leng -1):
            maxp += max(prices[i + 1] - prices[i], 0)
        return maxp