import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

class SegmentTree:
    def __init__(self, a, n):
        self.n = 1 << math.ceil(math.log2(n))
        self.t = [0] * self.n + a + [0] * (self.n - n)
        for i in range(self.n - 1, 0, -1): self.t[i] = self.t[i<<1] + self.t[i<<1|1]

    def query(self, l, r):
        v, l, r = 0, l + self.n, r + self.n
        while l < r:
            if l&1: l, v = l + 1, v + self.t[l]
            if r&1: r, v = r - 1, v + self.t[r - 1]
            l, r = l >> 1, r >> 1
        return v

    def update(self, i, x):
        i += self.n; d = x - self.t[i]; self.t[i] = x
        while i > 1: i >>= 1; self.t[i] += d


n, m = rrm()
a = rrm()
st = SegmentTree(a, n)

for _ in range(m):
    t, x, y = map(int, input().split())
    if t == 1: st.update(x, y)
    else: print(st.query(x, y))

## from walborn
