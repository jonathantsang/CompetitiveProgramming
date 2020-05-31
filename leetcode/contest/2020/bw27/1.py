class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c1 = Counter(target)
        c2 = Counter(arr)
        if len(c1) != len(c2):
            return False
        for d in c1:
            if d in c2 and c2[d] == c1[d]:
                pass
            else:
                return False
        return True
