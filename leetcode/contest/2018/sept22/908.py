class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        smallest = min(A)
        largest = max(A)
        if (smallest + K >= largest - K):
            return 0
        else:
            return (largest - K) - (smallest + K)