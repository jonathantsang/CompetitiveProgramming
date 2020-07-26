class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low

        amt = 0
        if low&1:
            # start at even
            amt = (diff-1)//2
        else:
            # start at odd
            amt = (diff)//2

        amt += (low&1) + (high&1)
        #print(low&1, high&1)
        return amt
