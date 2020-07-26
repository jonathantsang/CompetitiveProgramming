class Solution:
    def minFlips(self, target: str) -> int:
        flipped = 0
        ops = 0
        for v in target:
            if v == '0' and flipped == 1 or v == '1' and flipped == 0:
                flipped ^= 1
                ops += 1
        return ops
