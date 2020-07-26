class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        N = len(s)
        ans = ['' for _ in range(N)]
        for i,c in zip(indices,s):
            ans[i] = c
        return ''.join(ans)
            
