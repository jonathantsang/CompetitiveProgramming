class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # 2d dp
        # up to ith element, best dot product
        dp = [[-float('inf') for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        for i in range(len(nums1)+1):
            for j in range(len(nums2)+1):
                if i == 0 or j == 0:
                    continue
                # take the jth element for ith or skip
                a = dp[i][j-1]
                b = dp[i-1][j]
                c = dp[i-1][j-1]
                d = dp[i-1][j-1]
                if c == -float('inf'):
                    c = 0
                dp[i][j] = max(a, b, nums1[i-1] * nums2[j-1], nums1[i-1] * nums2[j-1] + c, d)
        ans = -float('inf')
        for r in dp:
            ans = max(ans, max(r))
            #print(r)
        return ans
                
