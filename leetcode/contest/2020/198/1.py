class Solution:
    def numWaterBottles(self, n: int, numExchange: int) -> int:
        amt = 0
        leftover_empty = 0
        while n > 0:
            amt += n
            total_empty = n + leftover_empty
            n = total_empty // numExchange
            leftover_empty = total_empty % numExchange

        return amt
