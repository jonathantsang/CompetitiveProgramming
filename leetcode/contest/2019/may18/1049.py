class Solution:
    minval = float('inf')

    def rungame(self, stones):
        queue = [stones]
        while len(queue) > 0:
            use = queue.pop()
            if len(use) == 0:
                continue
            if len(use) == 1:
                self.minval = min(self.minval, use[0])
                continue
            for i, stone1 in enumerate(use):
                for j, stone2 in enumerate(use, start=i+1):
                    # Clap em
                    if stone1 == stone2:
                        use.pop(max(i, j))
                        use.pop(min(i, j))
                    else:
                        if stone1 < stone2:
                            i =  j
                            stone1 = stone2
                        stone1 -= stone2
                        use.pop(j)
                    # Now have stones array that is removed
                    queue.append(stones)
            # At the end still use queue ones

    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.rungame(stones)
        return self.minval
        