import collections
class Monoqueue(collections.deque):
    def enqueue(self, val):
        count = 1
        while self and self[-1][0] > val:
            count += self.pop()[1]
        self.append([val, count])
    def dequeue(self):
        ans = self.min()
        self[0][1] -= 1
        if self[0][1] <= 0:
            self.popleft()
        return ans
    def min(self):
        return self[0][0] if self else 0
class Solution:
    def solve(self, A, K):
        #dp[i] = cost[i] + min(dp[i-1],... dp[i-K])
        mq = Monoqueue()
        for i, x in enumerate(A):
            r = mq.min() + x
            mq.enqueue(r)
            if i >= K:
                mq.dequeue()
        return r
