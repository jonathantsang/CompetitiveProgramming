from collections import Counter

class Solution:
    def solve(self, genes):
        N = len(genes)
        ps = list(range(N))

        look = {genes[i]: i for i in range(N)}

        def find(x):
            if x != ps[x]:
                ps[x] = find(ps[x])
            return ps[x]

        def merge(x, y):
            px, py = find(x), find(y)
            if px != py:
                ps[py] = px

        def same(s1,s2):
            if s1==s2:
                return True
            diff=0
            for c1,c2 in zip(s1,s2):
                if c1 != c2:
                    if diff == 0:
                        diff = 1
                    else:
                        return False
            return True

        for i in range(N):
            for j in range(len(genes[i]))
                for c in ['A','C','G','T']:
                    # enumerate letter
                    word = genes[i][:j]+c+genes[i][j+1:]
                    if word in look:
                        merge(i,look[word])

        count = set()
        for i in range(N):
            count.add(find(i))
        return len(count)
