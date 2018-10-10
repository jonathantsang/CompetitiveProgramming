class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        rightMaxVals = [A[0]]
        leftMinVals = [A[len(A)-1]]
        for i in range(1, len(A)):
            rightMaxVals.append(max(rightMaxVals[i-1], A[i]))
        
        for i in range(len(A)-2, -1, -1):
            leftMinVals.insert(0, min(leftMinVals[0], A[i]))
        
        bestIdx = len(A)-1
        for i in range(0, len(A)-1):
            if rightMaxVals[i] <= leftMinVals[i+1]:
                bestIdx = i+1
                return bestIdx
        return bestIdx