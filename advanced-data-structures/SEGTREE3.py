class SegmentTree:
    def __init__(self, a, n):
        import math
        # CHANGE
        self.defaultVal = 0

        self.n = 1 << math.ceil(math.log2(n))
        self.t = [self.defaultVal] * self.n + a + [self.defaultVal] * (self.n - n)
        for i in range(self.n - 1, 0, -1): self.t[i] = self.comparator(self.t[i<<1], self.t[i<<1|1])

    def query(self, l, r):
        # v = 0, default
        v, l, r = self.defaultVal, l + self.n, r + self.n
        while l < r:
            if l&1: l, v = l + 1, self.comparator(v, self.t[l])
            if r&1: r, v = r - 1, self.comparator(v, self.t[r - 1])
            l, r = l >> 1, r >> 1
        return v

    def update(self, i, x):
        i += self.n; d = x - self.t[i]; self.t[i] = x
        while i > 1: i >>= 1; self.t[i] = self.comparator(self.t[i], d)

    def comparator(self, v1, v2):
        # CUSTOM COMPARE
        # ex. for sum of range
        # return v1 + v2
        return v1 + v2

    def __repr__(self):
        return " ".join(list(map(str, self.t)))

    def __str__(self):
        return " ".join(list(map(str, self.t)))
