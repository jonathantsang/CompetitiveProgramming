import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))
INF=float('inf')

class SegmentTree():
    def __init__(self, a, n):

        # CHANGE
        self.defaultVal = float('inf')

        self.size = 1

        while self.size < n:
            self.size *= 2

        self.arr = [self.defaultVal] * (2 * self.size)

    def build2(self, A, x, lx, rx):
        if ((rx - lx) == 1):
            if lx < len(A):
                self.arr[x] = A[lx]
            return

        m = lx + rx >> 1

        self.build2(A, 2 * x + 1, lx, m)
        self.build2(A, 2 * x + 2, m, rx)

        self.arr[x] = self.comparator(self.arr[2 * x + 1],self.arr[2 * x + 2])

    def build(self, A):
        self.build2(A, 0, 0, self.size)

    def setV2(self, i, v, x, lx, rx):
        if ((rx - lx) == 1):
            # bottom level of segment tree
            self.arr[x] = v
            return

        m = lx + rx >> 1

        if i < m:
            # left child
            self.setV2(i, v, 2 * x + 1, lx, m)
        else:
            # right child
            self.setV2(i, v, 2 * x + 2, m, rx)

        self.arr[x] = self.comparator(self.arr[2 * x + 1],self.arr[2 * x + 2])

    def update(self, i, v):
        self.setV2(i, v, 0, 0, self.size)

    def queryV(self, l, r, x, lx, rx):
        if (lx >= r or l >= rx):
            return self.defaultVal # does not intersect

        if (lx >= l and rx <= r):
            return self.arr[x]

        m = lx + rx >> 1

        s1 = self.queryV(l, r, 2 * x + 1, lx, m)
        s2 = self.queryV(l, r, 2 * x + 2, m, rx)

        return self.comparator(s1,s2)

    # sums from l to r
    def query(self, l, r):
        return self.queryV(l, r, 0, 0, self.size)

    def comparator(self, v1, v2):
        # CUSTOM COMPARE
        # ex. for sum of range
        # return v1 + v2
        return min(v1,v2)

    def __repr__(self):
        return " ".join(list(map(str, self.arr)))

    def __str__(self):
        return " ".join(list(map(str, self.arr)))


n,m = rrm()
arr = rrm()

s = SegmentTree(arr, n)
s.build(arr)

ans = []
for _ in range(m):
    op, a, b = rrm()
    if op == 1:
        s.update(a, b)
    else:
        ans.append(str(s.query(a, b)))
print("\n".join(ans))
