class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = 0
        ones = 0
        for v in s:
            if v == '0':
                zeroes += 1
            elif v == '1':
                ones += 1

        best = 0
        left = 0
        right = ones
        for i in range(0, len(s)-1):
            if s[i] == '0':
                left += 1
            elif s[i] == '1':
                right -= 1
            best = max(best, left+right)
        return best
