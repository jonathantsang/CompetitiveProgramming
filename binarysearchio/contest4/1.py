class Solution:
    def solve(self, n, e, o, t):
        # Write your code here
        v = int(n)
        i = 0
        while v < t:
            if i % 2 == 0:
                v += v * (e / 100)
            else:
                v += v * (o / 100)
            i += 1
        return i