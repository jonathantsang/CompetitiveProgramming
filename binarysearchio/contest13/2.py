from collections import defaultdict

class Solution:
    def solve(self, matrix):
        if not matrix:
            return 0
        N,M=len(matrix),len(matrix[0])

        seen = set()
        def dfs(i,j, col):
            if not(0<=i<N) or not(0<=j<M):
                return
            if (i,j) in seen:
                return
            seen.add((i,j))
            for ix, ij in [(0,1), (0,-1), (1,0), (-1,0)]:
                ix += i
                ij += j
                if (0<=ix<N) and (0<=ij<M) and col == matrix[ix][ij]:
                    dfs(ix,ij,col)

        groups = defaultdict(int) # color -> group count
        totalgroups = 0
        for i in range(N):
            for j in range(M):
                if (i,j) not in seen:
                    groups[matrix[i][j]] += 1
                    dfs(i,j, matrix[i][j])
                    totalgroups += 1

        ans = float('inf')
        for col in groups:
            others = totalgroups - groups[col]
            ans = min(others, ans)
        return ans
