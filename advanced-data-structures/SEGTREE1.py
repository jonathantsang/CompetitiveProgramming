class SegmentTree():
    def __init__(self, n):
        self.size = 1

        while self.size < n:
            self.size *= 2

        self.arr = [0] * (2 * self.size)

    def build2(self, A, x, lx, rx):
        if ((rx - lx) == 1):
            if lx < len(A):
                self.arr[x] = A[lx]
            return

        m = lx + rx >> 1

        self.build2(A, 2 * x + 1, lx, m)
        self.build2(A, 2 * x + 2, m, rx)

        self.arr[x] = self.arr[2 * x + 1] + self.arr[2 * x + 2]

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

        self.arr[x] = self.arr[2 * x + 1] + self.arr[2 * x + 2]

    def setV(self, i, v):
        self.setV2(i, v, 0, 0, self.size)

    def sumV2(self, l, r, x, lx, rx):
        if (lx >= r or l >= rx):
            return 0 # does not intersect

        if (lx >= l and rx <= r):
            return self.arr[x]

        m = lx + rx >> 1

        s1 = self.sumV2(l, r, 2 * x + 1, lx, m)
        s2 = self.sumV2(l, r, 2 * x + 2, m, rx)

        return s1 + s2

    # sums from l to r
    def sumV(self, l, r):
        return self.sumV2(l, r, 0, 0, self.size)

    def __repr__(self):
        return " ".join(list(map(str, self.arr)))

    def __str__(self):
        return " ".join(list(map(str, self.arr)))

# small test
# a = [1,2,3,4,5,6,7]
#
# b = SegmentTree(7)
#
# # Set each val O(nlogn)
# for i,v in enumerate(a):
#     b.setV(i,v)
#
# # OR build in linear time
# b.build(a)
# print('summ', b.sumV(0,4))
