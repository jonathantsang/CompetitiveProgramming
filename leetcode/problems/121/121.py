class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices) < 2):
            return 0
        min = prices[0]
        bgain = 0
        for n in range(1, len(prices)):
            calc = prices[n] - min
            if(min > prices[n]):
                min = prices[n]
            if(calc > bgain):
                bgain = calc
        return bgain
            