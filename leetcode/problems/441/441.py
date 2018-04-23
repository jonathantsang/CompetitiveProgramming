class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        rows = 0
        while(count <= n):
            n = n - count
            count = count + 1
            rows = rows + 1
        return rows