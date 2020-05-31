class Solution:
    def solve(self, nums):
        n = len(nums)
        for i in range(n):
            nums[i] -= 1

        smaller = []
        st = SegmentTree(n+1)
        for i in range(n):
            smaller.append(st.query(0, nums[i]-1))
            st.update(nums[i], 1)

        larger = []
        st = SegmentTree(n+1)
        for i in range(n)[::-1]:
            larger.append(st.query(0, nums[i]-1))
            st.update(nums[i], 1)
        larger.reverse()

        MOD = 10**9 + 7
        total = ans = 0
        for i in range(n):
            ans += total * larger[i]
            ans %= MOD
            total += smaller[i]
            total %= MOD
        return ans


class SegmentTree(object):
    def __init__(self, size):
        from math import ceil, log2

        self.offset = 1 << ceil(log2(size))
        self.data = [0] * (2 * self.offset)

    # update value at index i
    def update(self, i, x):
        i += self.offset
        while i:
            self.data[i] += x
            i >>= 1

    # query max between indexes i and j inclusive
    def query(self, i, j):
        i += self.offset
        j += self.offset + 1
        ans = 0
        while i < j:
            if i & 1:
                ans += self.data[i]
                i += 1
            if j & 1:
                j -= 1
                ans += self.data[j]
            i >>= 1
            j >>= 1
        return ans

# from crabmilk
