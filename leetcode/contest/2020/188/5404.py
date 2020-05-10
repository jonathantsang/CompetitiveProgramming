class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        seen = set(target)
        stop = max(target)
        for i in range(1, stop+1):
            if i in seen:
                ops.append("Push")
            else:
                ops.append("Push")
                ops.append("Pop")
        return ops
