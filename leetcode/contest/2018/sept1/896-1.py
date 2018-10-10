class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increasing = True
        decreasing = True
        for i in range(1, len(A)):
            if(A[i-1] > A[i]):
                increasing = False
        for i in range(1, len(A)):
            if(A[i-1] < A[i]):
                decreasing = False
        return increasing or decreasing