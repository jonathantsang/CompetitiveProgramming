class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        go = set()
        to = set()
        for p in paths:
            go.add(p[0])
            to.add(p[1])
        c = to - go
        v = None
        for city in c:
            v = city
        return city
