class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A = list(map(lambda n: pow(n,2), A))
        A.sort()
        return A