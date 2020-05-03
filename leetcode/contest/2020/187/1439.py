import sortedcontainers

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n, m = len(mat), len(mat[0])
        s = sortedcontainers.SortedList([mat[0][i] for i in range(m)])
        for row in mat[1:]:
            temp = sortedcontainers.SortedList([row[i] + s[j] for i in range(len(row)) for j in range(len(s))])
            s = temp[:k]
        return s[k-1]
        
