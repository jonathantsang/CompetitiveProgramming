class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increasing = True
        decreasing = True
        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                if(increasing == False and decreasing == False):
                    return False
                if(A[i] > A[j]):
                    increasing = False
                elif(A[i] < A[j]):
                    decreasing = False
        return increasing or decreasing