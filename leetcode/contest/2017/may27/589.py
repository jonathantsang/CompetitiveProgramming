class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minX = 400001
        minY = 400001
        if(ops == []):
            return m * n
        for op in range(0, len(ops)):
            if(ops[op][0] < minX):
                minX = ops[op][0]
            if(ops[op][1] < minY):
                minY = ops[op][1]
        return minY * minX
        