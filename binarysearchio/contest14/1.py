class Solution:
    def solve(self, n):
        amt = 0
        leftover_empty = 0
        while n > 0:
            amt += n
            total_empty = n + leftover_empty
            n = total_empty // 3
            leftover_empty = total_empty % 3

        return amt
