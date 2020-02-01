class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        else:
            # possible
            u = []
            l = []
            for i in range(0, len(colsum)):
                if colsum[i] == 2:
                    u.append(1)
                    l.append(1)
                    upper -= 1
                    lower -= 1
                elif colsum[i] == 0:
                    u.append(0)
                    l.append(0)
                else:
                    # can be 1 in u or l
                    if upper > lower:
                        u.append(1)
                        l.append(0)
                        upper -= 1
                    else:
                        u.append(0)
                        l.append(1)
                        lower -= 1
                if lower < 0 or upper < 0:
                    return []
            return [u, l]