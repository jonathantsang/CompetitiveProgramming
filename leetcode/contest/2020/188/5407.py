class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9+7

        amt = 0
        @lru_cache(None)
        def cuts(c, x1, x2, y1, y2):
            amt = 0
            if c+1 == k:
                for i in range(y1, y2):
                    if 'A' in pizza[i][x1:x2]:
                        return 1
            else:
                validCut = False
                for i in range(x1, x2):
                    if not validCut and 'A' in [row[i] for row in pizza[y1:y2]]:
                        validCut = True
                    elif validCut and i > x1:
                        amt += cuts(c+1, i, x2, y1, y2)
                        amt %= MOD

                validCut = False
                for i in range(y1, y2):
                    if not validCut and 'A' in pizza[i][x1:x2]:
                        validCut = True
                    elif validCut and i > y1:
                        amt += cuts(c+1, x1, x2, i, y2)
                        amt %= MOD
            return amt % MOD
        return cuts(0, 0, len(pizza[0]), 0, len(pizza))
