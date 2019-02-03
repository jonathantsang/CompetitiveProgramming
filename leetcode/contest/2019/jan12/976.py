class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        x = len(A)-3
        y = len(A)-2
        z = len(A)-1
        best = 0
        while(x < z and y < z and x >= 0 and y >= 0 and z >= 0):
            # Valid
            if A[x] + A[y] > A[z]:
                best = max(best, A[x] + A[y] + A[z])
                x -= 1
                y -= 1
            else:
                z -= 1
                if z == y:
                    y -= 1
                    x -= 1
        return best