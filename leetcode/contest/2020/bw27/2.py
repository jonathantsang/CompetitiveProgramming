class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        limit = 2**k
        for i in range(0, limit):
            v = str(bin(i))[2:]
            # need to pad with 0s to match length
            if len(v) != k:
                v = (k - len(v)) * '0' + v
            if v in s:
                pass
            else:
                return False
        return True
