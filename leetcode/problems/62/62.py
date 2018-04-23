class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n - 2
        bigger = max(m-1, n-1)
        amt = total - bigger
        num = 1
        denom = 1
        i = 1
        while(i <= amt):
            num = num * total
            denom = denom * i
            total = total - 1
            i = i + 1
        return num/denom