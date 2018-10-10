class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        M = 1000000007
        minTotal = 0
        for i in range(0, len(A)):
            minSoFar = 999999999999
            for j in range(i, len(A)):
                minSoFar = min(minSoFar, A[j])
                minTotal += minSoFar
                minTotal %= M
        return int(minTotal)