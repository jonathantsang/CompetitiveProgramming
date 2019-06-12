# array A elements
# change sign for K elements
# change negatives to positive, smallest negatives first
# smallest number flip sign, alternate on the smallest value


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for i in range(0, K):
            smallest = A[0]
            smallestidx = 0
            for j, v in enumerate(A):
                if v < smallest:
                    smallest = v
                    smallestidx = j
            A[smallestidx] = -A[smallestidx]
        return sum(A)