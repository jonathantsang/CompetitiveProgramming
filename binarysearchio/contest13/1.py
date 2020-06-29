import math

class Solution:
    def solve(self, fractions):
        f = set()
        for n,d in fractions:
            g = math.gcd(n,d)
            while g != 1:
                n //= g
                d //= g
                g = math.gcd(n,d)
            f.add((n,d))
        ans = []
        for t,d in f:
            ans.append((t,d))
        ans = sorted(ans, key=lambda x: x[0]/x[1])
        return [[x,y] for x,y in ans]
