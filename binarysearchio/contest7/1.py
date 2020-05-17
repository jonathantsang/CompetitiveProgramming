class Solution:
    def solve(self, s):
        # Write your code here
        idx = -1
        side = 0 # 0 left, 1 right
        left = True
        right = True
        for i, d in enumerate(s):
            if side == 0 and d == 'B':
                left = False
            elif side == 1 and d == 'B':
                right = False
            if d == 'R':
                side = 1
        return left or right
