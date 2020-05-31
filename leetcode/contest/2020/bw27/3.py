class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        req = defaultdict(list)
        for c, p in prerequisites:
            req[c].append(p)

        ans = []
        for c, p in queries:
            need = set()

            q = deque([c])
            while q:
                v = q.popleft()
                if v in need:
                    continue
                need.add(v)

                q.extend(req[v])

            if p in need:
                ans.append(True)
            else:
                ans.append(False)

        return ans
