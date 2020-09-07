import collections

class MaxQueue(collections.deque):
    """
    A queue with O(1) max operations.
    """
    def enqueue(self, val):
        count = 1
        while self and self[-1][0] < val:
            count += self.pop()[1]
        self.append([val, count])

    def dequeue(self):
        ans = self.max()
        self[0][1] -= 1
        if self[0][1] <= 0:
            self.popleft()
        return ans

    def max(self):
        return self[0][0] if self else 0
